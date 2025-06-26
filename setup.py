from setuptools import setup, find_packages

setup(
    name="brainctl",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # or use pip -r requirements.txt instead
    ],
    entry_points={
        "console_scripts": [
            "brainctl = brainctl.cli:run",
        ]
    },
)

