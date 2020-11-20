import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()



#/Users/ericel123/Library/Python/3.8/bin
setuptools.setup(
    name="example-pkg-ericel123", # Replace with your own username
    version="0.0.3",
    author="Oj Obasi",
    author_email="ericel123@gmail.com",
    description="Testing Python Packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericel/pythonpackaging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)