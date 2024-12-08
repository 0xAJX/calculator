from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    author="Abhishek",
    author_email="abhi@jadhav.io",
    description="A simple calculator package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0xajx",  # Optional
    packages=find_packages(),  # Automatically find sub-packages
    install_requires=[],  # List dependencies here or use requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)