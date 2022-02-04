import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="artdirector",
    version="0.0.1",
    author='Johannes Daniel Nümm',
    author_email='daniel.nuemm@blacktre.es',
    description='Art directed image cropping',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jdnumm/artdirector',
    project_urls={
        "Bug Tracker": "https://github.com/jdnumm/artdirector/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
