# from distutils.core import setup
from setuptools import setup

projectName = "TraVersion"
packageName = "traVer"
initFile = "./%s/__init__.py" % packageName
version = None
with open(initFile) as fd:
    exec(fd.read())
    version = __version__

with open("README.md") as fd:
    readmeData = fd.read()

with open("LICENSE") as fd:
    licenseData = fd.read()

setup(
    name=packageName,
    description="Semantic versioning for python projects",
    version=version,
    packages=[
        packageName,
    ],
    license=licenseData,
    long_description=readmeData,
    author="Sunil Kumar Nerella",
    author_email="sunil.nerella39@gmail.com",
    data_files=[
        "./README.md",
        "./LICENSE"
    ],
)
