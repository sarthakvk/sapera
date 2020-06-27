from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sapera",
    version="2.0",
    author="Sarthak Vineet Kumar",
    author_email="sarthakchaudhary13@gmail.com",
    description="A python package for learning algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarthakchaudhary13/sapera",
    packages=find_packages() + ["data"],
    include_package_data=True,
    licence="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "scrapy",
    ],
    # entry point for the application
    entry_points={
        "console_scripts": [
            "sapera=sapera:entry_point",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/sarthakchaudhary13/sapera/issues",
        "Say Thanks!": "http://svkumar.me",
        "Source": "https://github.com/sarthakchaudhary13/sapera/",
        "Algorithms Source": "https://github.com/sarthakchaudhary13/Python",
    },
)
