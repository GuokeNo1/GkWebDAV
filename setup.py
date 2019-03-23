import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gkwebdav",
    version="0.0.1",
    author="Guoke",
    author_email="1962908113@qq.com",
    description="new Webdav Client for Python3+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GuokeNo1/Gkwebdav",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)