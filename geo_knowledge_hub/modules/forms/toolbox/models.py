# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 GEO Secretariat.
#
# geo-knowledge-hub is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""GEO Knowledge Hub Forms."""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField
)

from wtforms.validators import (
    DataRequired, Email, Length
)


class BecomeAKnowledgeProviderForm(FlaskForm):
    """Form to become a Knowledge Provider on the GEO Knowledge Hub platform."""
    name = StringField(
        "Name",
        [
            DataRequired()
        ]
    )

    email = StringField(
        "Email",
        [
            Email(message="Invalid email!"),
            DataRequired()
        ]
    )

    text = TextAreaField(
        "Why would I want to be a knowledge provider ?",
        [
            Length(min=4, message="Your message is too short"),
            DataRequired()
        ]
    )

    submit = SubmitField("Submit")


__all__ = (
    "BecomeAKnowledgeProviderForm"
)
