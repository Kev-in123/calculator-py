from setuptools import setup, find_packages

version = "1.2.0"

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.readlines()

setup(
    name="calculator_py",
    version=version,
    description="This package is a simple calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kev-in123",
    author_email="kevinchoi005@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires = requirements,
    python_requires = ">=3.6",
    url = "https://github.com/Kev-in123/calculator-py", 
    project_urls={
    "Issue tracker": "https://github.com/Kev-in123/calculator-py/issues",
    },
)

