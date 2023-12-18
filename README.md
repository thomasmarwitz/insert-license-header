# Tool: insert-license-header
This python script automatically inserts your license header at the beginning of specified source code files.

Forked from [Lucas-C/pre-commit-hooks](https://github.com/Lucas-C/pre-commit-hooks) and modified to realize the following behaviour:

> :warning: The behaviour of `--dynamic-years` changed in version `1.1.0`.
>
Add argument `--dynamic-years` which determines the start year of the copyright time range automatically - based on when
the file was first tracked with Git. If a start year is already present, it is not touched.
If a file is not tracked by Git, the current year is used as start year.
The end year is automatically set to the date of the last commit that affected the file.
If an end year is already present that is in the future, don't touch it. It is, however,
incremented if it lies in the past. If the file is not tracked by Git, use the current year.

Include a `{year_start}` and `{year_end}` in your license header to use this feature.

Add argument `--license-base64` to include a license not via a file but through
a `base64` encoded string that is passed as a value for this argument.
Obtain your license `base64` encoded string with `cat LICENSE.txt | base64`.
Including a license via `--license-base64 {base64string}` overrides the
`--license-filepath` option.

> :warning: This is not a pre-commit hook anymore. Instead, this repository contains just the base script to insert licenses in text-based files. To check out the resulting pre-commit hook, visit: https://github.com/Quantco/pre-commit-insert-license
