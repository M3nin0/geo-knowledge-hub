# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 GEO Secretariat.
#
# geo-knowledge-hub is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

from flask import Blueprint

from . import views


def init_bp(app):
    bp = Blueprint("geo_forms_bp", __name__, template_folder="theme/templates")

    # registration
    bp.add_url_rule("/forms/become-provider", "form_become_provider", views.form_view_become_knowledge_provider)

    app.register_blueprint(bp)


__all__ = (
    "init_bp"
)
