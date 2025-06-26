from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("dev-requirements.txt") as f:
    dev_requires = f.read().splitlines()

setup(
    name="brainctl",
    version="0.1.0",
    description="Rick-powered infrastructure automation CLI",
    author="DesertBlume",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires
    },
    entry_points={
        "console_scripts": [
            "brainctl = brainctl.cli:run",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

