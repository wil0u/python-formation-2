from setuptools import find_packages, setup

setup(
    name="operations-basique",
    version="0.1.0",
    description="Basic arithmetic helpers",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
)
