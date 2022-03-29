# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-knowledge-hub is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

from pydash import py_
from flask import render_template

from invenio_app_rdm.records_ui.views.decorators import (
    pass_is_preview,
    pass_record_files,
    pass_record_or_draft,
)

from invenio_rdm_records.resources.serializers import UIJSONSerializer

from .toolbox.search import get_related_resources_metadata
from .toolbox.identifiers import related_identifiers_url_by_scheme
from .toolbox.vocabulary import get_engagement_priority_from_record


@pass_is_preview
@pass_record_or_draft
@pass_record_files
def geo_record_detail(record=None, files=None, pid_value=None, is_preview=False):
    """Record detail page (aka landing page)."""
    # Base definitions
    files_data = None if files is None else files.to_dict()

    record_data = record.to_dict()
    record_ui = UIJSONSerializer().serialize_object_to_dict(record_data)

    # General record properties
    record_is_draft = record_ui.get("is_draft")

    # Related records
    all_related_records_informations = get_related_resources_metadata(
        record_data.get("metadata")
    )

    related_records_informations, user_stories = py_.partition(
        all_related_records_informations,
        lambda x: py_.get(x, "ui.resource_type.id") != "user-story",
    )

    # Identifiers
    related_identifiers = related_identifiers_url_by_scheme(
        py_.get(record_data, "metadata.related_identifiers", [])
    )

    # Removing all related resource that is a knowledge resource
    related_identifiers = py_.filter(
        related_identifiers,
        lambda x: x["identifier"].split("/")[-1]
        not in py_.map(
            all_related_records_informations,
            lambda y: y["id"],
        ),
    )

    # Engagement priorities
    engagement_priorities_scheme = ["TU", "EP"]
    related_engagement_priorities = get_engagement_priority_from_record(
        record, engagement_priorities_scheme
    )

    # Removing all engagement priorities from the record
    # temporary solution: in the future, we will remove this!
    def _get_subject_metadata(subject, subjects_metadata):
        for subject_metadata in subjects_metadata:
            if "id" in subject and subject["id"] == subject_metadata["id"]:
                subject["scheme"] = py_.get(subject_metadata, "props.scheme")
        return subject

    _engage_ids_without_icon = (
        py_.chain(related_engagement_priorities)
        .filter(lambda x: py_.get(x, "props.icon") == "")
        .map(lambda x: x["id"])
    ).value()

    record_subjects, geo_subjects = (
        py_.chain(record_ui)
        .get("metadata.subjects")
        .filter(
            lambda x: (
                "scheme" in x and x["scheme"] not in engagement_priorities_scheme
            )
            or (
                "scheme" in x
                and x["scheme"] == "EP"
                and x["id"] in _engage_ids_without_icon
            )
            or ("scheme" not in x)
        )
        .map(lambda x: _get_subject_metadata(x, related_engagement_priorities))
        .partition(
            lambda x: "id" not in x or ("id" in x and "geo" not in x["id"].lower())
        )
    ).value()

    record_ui = py_.set(record_ui, "metadata.subjects", record_subjects)

    # preparing the geo subjects
    def _style_fnc(x):
        name = x["subject"][x["subject"].find("(") + 1 : x["subject"].find(")")]
        # styling the name
        if "-" in name:
            prefix, project = name.split("-")

            name = " ".join([prefix.upper(), project.title()])
        return name

    geo_subjects = py_.map(geo_subjects, _style_fnc)

    return render_template(
        "geo_knowledge_hub/records/detail.html",
        pid=pid_value,
        record=record_ui,
        files=files_data,
        is_draft=record_is_draft,
        is_preview=is_preview,
        related_identifiers=related_identifiers,
        geo_subjects=geo_subjects,
        user_stories=user_stories,
        related_records_informations=related_records_informations,
        related_engagement_priorities=related_engagement_priorities,
        permissions=record.has_permissions_to(
            ["edit", "new_version", "manage", "update_draft", "read_files"]
        ),
    )
