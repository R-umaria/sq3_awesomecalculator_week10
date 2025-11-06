from setuptools import setup, find_packages

setup(
    name="awesomecalculator-rishi",  # unique name for TestPyPI
    version="1.0.1",
    author="Rishi Umaria",
    author_email="rishiumaria24@gmail.com",
    description="An awesome calculator package with add, subtract, multiply, and divide functions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rishiumaria/sq3_awesomecalculator_week10",
    packages=find_packages(include=['calculator', 'calculator.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
