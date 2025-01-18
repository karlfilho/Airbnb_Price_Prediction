from setuptools import setup, find_packages

setup(
    name="airbnb-price-prediction",
    version="2.0.0",
    author="Karl Filho",
    author_email="karlfilho@gmail.com",
    description="Airbnb price prediction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/karlfilho/airbnb-price-prediction",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
