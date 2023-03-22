import io, pathlib
from setuptools import setup, find_packages

version_data = {}
version_file = pathlib.Path(__file__).parent / 'databricks/sdk/version.py'
with version_file.open('r') as f:
    exec(f.read(), version_data)

# look at this one
# https://github.com/psf/requests/blob/main/setup.py

setup(name="databricks",
      version=version_data['__version__'],
      packages=find_packages(exclude=["tests", "*tests.*", "*tests"]),
      python_requires=">=3.7",
      install_requires=["requests>=2.28.1", ],
      extras_require={"dev": ["pytest", "pytest-cov", "pytest-xdist", "yapf", "pycodestyle", "autoflake", "isort", "wheel"]},
      author="Serge Smertin <serge.smertin@databricks.com>",
      description="Official Databricks SDK for Python",
      long_description=io.open("README.md", encoding="utf-8").read(),
      classifiers=[
          "Intended Audience :: Developers",
          "Intended Audience :: System Administrators",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11"],
      keywords="databricks sdk",
      url="https://github.com/databricks/databricks-sdk-py")
