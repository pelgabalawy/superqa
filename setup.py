import setuptools
import _shared_.get_drivers as drivers

with open("README.md", "r") as fh:
    long_description = fh.read()

# download the chrome and firefox driver when pip installing the package
drivers.download_drivers()

setuptools.setup(
    name="superqa-pelgab", # Replace with your own username
    version="0.0.1",
    author="pelgabalawy",
    author_email="pelgabalawy@gmail.com",
    description="automated testing project to make life easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

