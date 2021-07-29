# Development Readme

## Package distribution: Pip 

## Continuous Integration Testing: pytest, Codecov, and Github Actions

Install pytest

```bash
pip install pytest
```

Install coverage

```bash
pip install coverage
```

Write tests in a 'tests' directory, then run them with:

```bash
pytest tests/\*
```

Run coverage with pytest to get coverage report:

```bash
coverage run -m pytest tests/\*
```

View coverage report

```bash
coverage report
```




https://about.codecov.io/blog/python-code-coverage-using-github-actions-and-codecov/

## Documentation

### Embed real example code in Github README

Using:
https://github.com/zakhenry/embedme#why

Install with `npx install embedme`

In README.md, create a code block with the filename of the code file to be embedded as a comment. 
Use `py` to signal Python language.

For example,
> \```py
> 
> \# readme_example_code.py
> 
> \```

Run `npx embedme README.md` to embed the code.
