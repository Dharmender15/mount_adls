import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="mount_adls_gen2",
    version="0.0.1",
    author="Ritwick Bhargav",
    author_email="ritwick.a.bhargav@accenture.com",
    description="Package to mount ADLS Gen2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)