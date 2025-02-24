Changelog
------------

2.1 (unreleased)
~~~~~~~~~~~~~~~~

- Nothing changed yet.


2.0 (2022-03-21)
~~~~~~~~~~~~~~~~

- Add Plone 6 support, remove <includeDependencies />
- Update test
- Housekeeping Code
- Update setup, tox.ini
  [1letter]

- Remove Plone 5.0 classifier as this version is not tested anymore.
  [thet]

- Format code according to Plone standards: black, isort, zpretty.
  [thet]

- Add uninstall profile.
  [thet]

- Update to Python3
  [1letter]

- Add plone.autoform.directives Support for Widget
- Add css klass to Widget
  [1letter]

- Add missing english translation file
  [thomasmassmann]

- Update translations.
  [thomasmassmann]


1.4.4 (2016-07-20)
~~~~~~~~~~~~~~~~~~

- Add Russian translation
  [serge73]

1.4.3 (2016-07-08)
~~~~~~~~~~~~~~~~~~

- Add macro for html forms
  [cekk]


1.4.2.2 (2013-04-25)
~~~~~~~~~~~~~~~~~~~~

- added italian translation
  [keul]

1.4.2.1 (2013-01-17)
~~~~~~~~~~~~~~~~~~~~

- add Dutch Translations
  [maartenkling]

1.4.2 (2012-10-03)
~~~~~~~~~~~~~~~~~~

- Add compatibility for collective.pfg.norobots : allow to use the Norobots captcha with PloneFormGen.
  [sylvainb]

- Fix widget template to allow good redirection when the answer is bad in plone.app.discussion forms.
  [sylvainb]

- Move source code in "src" directory.
  [sylvainb]

- Update tests, buildouts and add test coverage. Plone 4.0 is no longer supported.
  [sylvainb]

- Change MessageFactory name to get translations picked up by Plone
  [erral]

- Updated basque translation and added Spanish translation.
  [erral]

1.4.1 (2012-07-02)
~~~~~~~~~~~~~~~~~~

- Fix Unicode error when a question contains non-ascii char.
  [sylvainb, Helmut Toplitzer]

1.4 (2012-06-22)
~~~~~~~~~~~~~~~~

- Use plone.app.registry instead of a property sheet for the questions configuration.
  Questions can now be added using a dedicated control panel.
  [sylvainb]

- Add an upgrade step (1 -> 2) to copy questions from the old properties sheet to plone.app.registry.
  [sylvainb]

- Fix the widget template for use with plone.app.discussion (there was no redirection to
  the comment form when only the captcha is wrong).
  [sylvainb]

- Update translations (some new strings added).
  [sylvainb]

- Add Basque translation
  [erral]


1.3.1 (2012-03-28)
~~~~~~~~~~~~~~~~~~~~~~~~

- Add simplified chinese translation
  [Aijun Jian]

1.3 (2012-02-27)
~~~~~~~~~~~~~~~~~~~~~~~~

- Allow multiple answers for a question
  [naro]

- Added danish translation
  [tmog]


1.2.1 (2010-11-05)
~~~~~~~~~~~~~~~~~~~~~~~~

- Added german translation
  [petschki]


1.2 (2010-10-31)
~~~~~~~~~~~~~~~~~~~~~~~~

- Fix tests for Plone 4
  [sylvainb]

- Added Czech translation
  [naro]

1.1 (2010-09-15)
~~~~~~~~~~~~~~~~~~~~~~~~

- Support for using as a plone.app.discussion captcha plugin (Plone 4)
  [Petri Savolainen]

- Finnish translations
  [Petri Savolainen]

1.0 (2010-01-13)
~~~~~~~~~~~~~~~~~~~~~~~~

- Initial release
  [sylvainb]
