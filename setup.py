import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-solc-simple",
    version="0.0.8",
    author="Paul Peregud",
    author_email="paulperegud@gmail.com",
    description="Simple wrapper around py-solc. Needs solc binary in PATH",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulperegud/py_solc_simple",
    packages=setuptools.find_packages(),
    classifiers=(
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points = {
        'console_scripts': ['py-solc-simple=solc_simple.builder:main'],
    },
    install_requires=[
        'web3==4.5.0',
        'py-solc==3.1.0'
    ]
)
