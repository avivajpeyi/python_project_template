from setuptools import find_packages, setup
import os
import codecs
import os
import re

NAME = "project_name"
PACKAGES = find_packages(where="project_name")
META_PATH = os.path.join("project_name", "__init__.py")
INSTALL_REQUIRES = [
    "numpy",
    "matplotlib"
]
EXTRA_REQUIRE = {"test": ["pytest>=3.6"]}
EXTRA_REQUIRE["dev"] = EXTRA_REQUIRE["test"] + [
    "pre-commit",
    "flake8",
    "black<=21.9b0",
    "isort",
]

# END PROJECT SPECIFIC

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]

HERE = os.path.dirname(os.path.realpath(__file__))
def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def find_meta(meta, meta_file=read(META_PATH)):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), meta_file, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setup(
    name=NAME,
    use_scm_version={
        "write_to": os.path.join(
            NAME, "{0}_version.py".format(NAME)
        ),
        "write_to_template": '__version__ = "{version}"\n',
    },
    author=find_meta("author"),
    author_email=find_meta("email"),
    maintainer=find_meta("author"),
    maintainer_email=find_meta("email"),
    url=find_meta("uri"),
    license=find_meta("license"),
    description=find_meta("description"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=PACKAGES,
    keywords=[],
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRE,
    classifiers=CLASSIFIERS,
    zip_safe=True,
    entry_points={
            "console_scripts": []
        },
)
