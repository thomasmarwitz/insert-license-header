=========
Changelog
=========


Insert-license-header 1.3.0
================================================
* Fix issue #9: Avoid needing to re-run insert-license-header tool in cases where a
  modification would lead to a newer git end year that is not yet present in the file.
* Detect whether in a shallow git repo, if yes, don't trust GIT
* Remove verbose output logs


Insert-license-header 1.2.0
================================================
* Added debugging functionality, can be triggered by providing `--debug`.


Insert-license-header 1.1.0
================================================
* Re-implement behaviour `--dynamic-years`
    * The end year is now also determined by GIT, the current year is NOT automtically used.
    * Effectively, the tool will not upgrade the year of files that have not been touched,
      this is important when using the pre-commit hook of this tool. Prior `1.1.0`,
      `pre-commit run insert-license -a` would cause your CI to go red after New Year's Eve.
* Fix link to the actual pre-commit repository.

Insert-license-header 1.0.2
================================================
* Make function that determines git start date more robust
    * If, e.g. no GIT repository exists, the tool will no longer fail but use the current year.
    * The path to the file is escaped, allowing for more crazy file names.

Insert-license-header 1.0.1
================================================
* (Re-trigger publishing workflow)

Insert-license-header 1.0.0 (2023-11-07)
================================================
* Tool is a standalone pypi tool and no longer a pre-commit hook
    * Rename project to `insert-license-header`
* Remove hard-coded default LICENSE.header
* Introduce `--license-base64` flag that allows to pass a base64 encoded license instead of specifying a file path via `--license-filepath`


Pre-commit-insert-qc-license v1.7.1 (2023-11-07)
================================================
* Refactoring
    * Remove unnecessary pre-commit-hooks
    * Rename module folder `pre-commit-hooks` to `pre-commit-insert-qc-license`
    * `default_license.py` => `LICENSE.header`
* Port project to use exclusively `pyproject.toml`
* Add Python `3.12` to CI


Pre-commit-insert-qc-license v1.7.0 (2023-10-25)
================================================
* Introduce `--dynamic-years` flag
* Option to omit `--license-filepath`: default QC license is taken from `pre-commit-hooks/default_license.py`
* Add execution of `pytest` to CI workflow

