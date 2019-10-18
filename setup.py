import io
from setuptools import setup

with io.open("README.md", encoding="utf-8") as f:
    README = f.read()


setup(
    name="pipfile-requirements",
    version="0.1.1",
    description="A CLI tool to covert Pipfile/Pipfile.lock to requirments.txt",
    url="https://github.com/frostming/pipfile-requirements",
    long_description=README,
    author="Frost Ming",
    py_modules=["pipfile_requirements"],
    author_email="mianghong@gmail.com",
    license="MIT",
    install_requires=["requirementslib"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["pipfile2req = pipfile_requirements:main"]},
)