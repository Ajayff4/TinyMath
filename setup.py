import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TinyMath",
    version="0.0.1",
    author="Ajay Agrawal",
    author_email="ajayff4@gmail.com",
    description="A small mathematics library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ajayff4/testing2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
