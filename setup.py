import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyLcSnap7-epics", # Replace with your own username
    version="0.0.1",
    author="Epics",
    author_email="d.kummer0702@gmail.com",
    description="My first example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DominikK0702/Snap7-PLC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha"
    ],
    python_requires='>=3.6',
)