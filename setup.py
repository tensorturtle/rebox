import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="rebox",
    version="0.1.1",
    description="Convert between bounding box annotation formats",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorturtle/bboxconvert",
    author="Jason Sohn",
    author_email="tensorturtle@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["rebox"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
        ]
    },
)
