# Development Readme

## Package distribution: Pip 

## Continuous Integration Testing: pytest, Codecov, and Github Actions

https://about.codecov.io/blog/python-code-coverage-using-github-actions-and-codecov/

## Documentation

### Embed real example code in Github README

Using:
https://github.com/zakhenry/embedme#why

Install with `npx install embedme`

In README.md, create a code block with the filename of the code file to be embedded as a comment. 
Use `py` to signal Python language.

For example, (without escape backslash)
> \```py
> # readme_example_code.py
> \```

Run `npx embedme README.md` to embed the code.
