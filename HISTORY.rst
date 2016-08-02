.. :changelog:

History
-------

2.3.0 (2015-08-02)

* Created a customized string-to-tag parser to match Selectize.js functionality
* No longer delimits tags based on spaces
* Added support for custom delimiter in settings
* WHEN UPGRADING: This should be backwards-compatible for existing behavior, but to fix a subtle Selectize bug with
  single tags with spaces, and to support custom DELIMITERs, please configure TAGGIT_TAGS_FROM_STRING and
  TAGGIT_STRING_FROM_TAGS as described in the README.

0.1.0 (2014-01-01)
++++++++++++++++++

* First release on PyPI.
