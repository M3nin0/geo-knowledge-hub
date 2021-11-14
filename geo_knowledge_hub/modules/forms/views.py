# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 GEO Secretariat.
#
# geo-knowledge-hub is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

from flask import (
    request,
    url_for,
    redirect,
    current_app,
    render_template,
)
from flask_mail import Message

from .toolbox.models import BecomeAKnowledgeProviderForm


def form_view_become_knowledge_provider():
    """Render form to request a Knowledge Provider access."""

    form = BecomeAKnowledgeProviderForm()
    form.process(request.form)

    if form.validate_on_submit():
        message = Message(
            f"Geo Knowledge Hub Registration",
            recipients=[
                current_app.config.get(
                    "GEO_KNOWLEDGE_HUB_EXT_DEFAULT_MAIL_RECEIVER"
                ),
                form.email.data
            ],
            body=f"Thank you {form.name.data} for your subscription"
        )

        current_app.extensions["mail"].send(message)
        return redirect(url_for("request_access_page"))
    return render_template(
        "geo_knowledge_hub/forms/form_request_provider_access.html",
        form=form,
        template="form-template"
    )


__all__ = (
    "form_view_become_knowledge_provider"
)
