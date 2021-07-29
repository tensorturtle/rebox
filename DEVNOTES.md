# Development Readme


## Package distribution: Pip 

## Continuous Integration Testing: pytest, Codecov, and Github Actions

### Testing Example

![](assets/albumentations_bbox_example.jpg)

An example image from the COCO dataset.

#### [From Albumentations documentation](https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/#albumentations)

| Format | Coordinates |
|---|---|
| YOLO | [0.4046875, 0.840625, 0.503125, 0.24375] |
| COCO | [98, 345, 322, 117]
| Pascal VOC | [98, 345, 420, 462] |
| Albumentations | [0.153125, 0.71875, 0.65625, 0.9625] |

#### Extras

| Format | Coordinates | 
| --- | --- | 
| Label Studio | [15.3125, 71.875, 65.625, 96.25] | 


### Workflow

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
pytest tests/*
```

Run coverage with pytest to get coverage report:

```bash
coverage run -m pytest tests/*
```

View coverage report

```bash
coverage report
```

**Resources**:
[Codecov Github Actions](https://about.codecov.io/blog/python-code-coverage-using-github-actions-and-codecov/)

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

### Automatically generate documentation from docstrings:

Sphinx with autodoc plugin
