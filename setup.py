from setuptools import setup, find_packages
import setuptools

setup(
    name="prompt_security",
    version="0.1.0",
    description="A brief description of your project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="",
    author="",
    author_email="",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # List your project's dependencies here
        "requests",
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "your_command=your_package.module:function",
        ],
    },
    include_package_data=True,
    package_data={
        # Include any data files that need to be bundled with the package
        "": ["*.txt", "*.md"],
    },
)
