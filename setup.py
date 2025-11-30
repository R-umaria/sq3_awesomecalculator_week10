from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    author="Rishi Umaria",
    author_email="rumaria6371@conestogac.on.ca",
    description="A simple calculator package from Week 10.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/R-umaria/sq3_awesomecalculator_week10",

    package_dir={'': 'src'},
    packages=find_packages(where='src'),

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
