from setuptools import setup, find_packages

setup(
    name="students_performance",
    version="0.0.1",
    author="Devakrishnan",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)