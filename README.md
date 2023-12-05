# pre-commit-insert-license
This pre-commit hook automatically inserts our license header at the beginning of specified source code files.

Forked from [Lucas-C/pre-commit-hooks](https://github.com/Lucas-C/pre-commit-hooks) and modified to realize the following behaviour:

Copyright header is inserted automatically in files checked by pre-commit.

Add argument `--dynamic-years` which determines the start year of the copyright time range automatically - based on when
the file was first tracked with Git. If a start year is already present, it is not touched.
If a file is not tracked by Git, the current year is used as start year.
The end year is automatically set to the current year
(`--use-current-year` is activated automatically when `--dynamic-years` is present).

Add argument `--license-base64` to include a license not via a file but through
a `base64`` encoded string that is passed as value for this argument.
Obtain your license `base64` encoded string with `cat LICENSE.txt | base64`.
Including a license via `--license-base64 {base64string}` overrides the
`--license-filepath` option.

Usage: (in `.pre-commit-config.yaml`)

```
- repo: https://github.com/Quantco/pre-commit-insert-qc-license
    rev: v1.7.2
    hooks:
      - id: insert-license
        files: \.py$
        args:
          - --dynamic-years
          - --comment-style
          - "#"
```

Other comment styles:
For Java / Javascript / CSS/ C / C++ (multi-line comments) set: `/*| *| */`
For Java / Javascript / C / C++ (single line comments) set `//`
For HTML files: `<!--|  ~|  -->`

To remove all license headers, temporarily add the `--remove-header` arg in
your `.pre-commit-config.yaml`. Run the hook on all files: `pre-commit run insert-license -a`.

For more configuration options see [Lucas-C/pre-commit-hooks](https://github.com/Lucas-C/pre-commit-hooks) and [Pre-Commit](https://pre-commit.com/)
