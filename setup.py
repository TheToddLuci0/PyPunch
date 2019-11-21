import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    include_package_data=True,
    name="PyPunch",
    version="1.0.0",
    author="TheToddLuci0",
    description="A Punchcard generation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheToddLuci0/PyPunch",
    packages=setuptools.find_packages(),
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires='>=3',
    install_requires=['pillow'],
    keywords=["punchcard", ],
)
