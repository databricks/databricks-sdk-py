import io, pathlib
from setuptools import setup, find_packages

version_data = {}
version_file = pathlib.Path(__file__).parent / 'databricks/sdk/version.py'
with version_file.open('r') as f:
    exec(f.read(), version_data)

setup(name="databricks-sdk",
      version=version_data['__version__'],
      packages=find_packages(exclude=["tests", "*tests.*", "*tests"]),
      python_requires=">=3.7",
      install_requires=["requests>=2.28.1,<2.29.0"],
      extras_require={"dev": ["pytest", "pytest-cov", "pytest-xdist", "pytest-mock",
                              "yapf", "pycodestyle", "autoflake", "isort", "wheel"]},
      author="Serge Smertin",
      author_email="serge.smertin@databricks.com",
      description="Databricks SDK for Python (Experimental)",
      long_description=io.open("README.md", encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      url="https://github.com/databricks/databricks-sdk-py",
      keywords="databricks sdk",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Operating System :: OS Independent"])
