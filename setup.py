import setuptools

with open("README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="JEGmail",
    version="0.0.0.0.1",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="JE use Gmail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JE-Chen/Python_Gmail_JE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
    ]
)

# sdist bdist_wheel
# python -m twine upload dist/*
