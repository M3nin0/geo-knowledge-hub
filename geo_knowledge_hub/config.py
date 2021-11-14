# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 GEO Secretariat.
#
# geo-knowledge-hub is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""GEO Knowledge Hub extension for InvenioRDM"""

from .security.policies import GeoRecordPermissionPolicy
from .security.permissions import views_permissions_factory

GEO_KNOWLEDGE_HUB_EXT_BASE_TEMPLATE = "geo_knowledge_hub/base/base.html"
"""Default base template for the demo page."""

GEO_KNOWLEDGE_HUB_EXT_SIDE_BAR_ELEMENTS = [
    "geo_knowledge_hub/records/details/side_bar/versions.html",
    "geo_knowledge_hub/records/details/side_bar/related_identifiers.html",
    "geo_knowledge_hub/records/details/side_bar/export.html"
]

GEO_KNOWLEDGE_HUB_EXT_INFORMATION_REQUIRED_IN_METADATA_BY_SCHEME = {
    "doi": {
        "id": "id",
        "title": "metadata.title",
        "resource_type": "metadata.resource_type.title.en",
        "description": "metadata.description"
    }
}
"""Default values to load from metadata by scheme type."""

GEO_KNOWLEDGE_HUB_EXT_DEFAULT_MAIL_RECEIVER = "gkhub@geosec.org"
"""Flask-Mail Default Email receiver."""

RDM_PERMISSION_POLICY = GeoRecordPermissionPolicy
"""Policy settings."""

GEO_KNOWLEDGE_HUB_VIEW_PERMISSIONS_FACTORY = views_permissions_factory
"""View permissions factory."""

# See Flask-Mail configurations options at:
#   https://pythonhosted.org/Flask-Mail/#configuring-flask-mail
"""Flask-Mail"""

# See Flask-Discussion (for Isso engine) options for Isso at:
#   https://flask-discussion.readthedocs.io/en/latest/configs/isso.html
"""Flask-Discussion"""
