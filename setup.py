from setuptools import setup, find_packages

setup(
    name="aipipe",
    version="0.1.0",
    packages=find_packages(exclude=['*.env', '*.env.*']),
    install_requires=[
        "openai>=1.0.0",
        "click>=8.0.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "aipipe=aipipe.cli:main",
        ],
    },
    author="x-zx",
    author_email="zzx094@gmail.com",
    description="AI pipeline command line tool for processing data with prompts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/x-zx/aipipe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 