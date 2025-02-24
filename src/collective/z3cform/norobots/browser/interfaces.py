# -*- coding: utf-8 -*-
from collective.z3cform.norobots.i18n import norobotsMessageFactory as _
from zope import schema
from zope.interface import Interface


class INorobotsWidgetSettings(Interface):
    """plone.app.registry settings"""

    questions = schema.Tuple(
        title=_("Norobots question::answer"),
        description=_(
            "Questions list (one per line). Example : 'What is 10 + 12 ?::22'. \
Answer can contain multiple values delimited by semicolon. Example : 'What is 5 + 5 ?::10;ten'."
        ),
        value_type=schema.TextLine(),
        required=True,
    )


class INorobotsView(Interface):
    """Norobots question generating and verifying view

    Usage:

        - Use the view from a page to get a question. Use the 'get_question' method.

        - The user will answer the question, and tell the server through a form
          submission.

        - Use the user input to verify.
    """

    def get_question():
        """Return a random question: {'id': '...', 'title': '...', 'id_check': '...'}"""

    def verify(input, question_id=None, id_check=None):
        """Verify the user-supplied input for a question id and is corresponding id_check.

        If question_id is None, the question id is find in REQUEST.form['question_id'].
        If id_check is None, the question id is find in REQUEST.form['id_check'].

        Returns a boolean value indicating if the input matched
        """
