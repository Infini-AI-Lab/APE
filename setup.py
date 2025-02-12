from setuptools import setup, find_packages

__version__ = '0.0.0'

setup(
    name="ape",
    version=__version__,
    author="Xinyu Yang",
    author_email='xinyuya2@andrew.cmu.edu',
    url='',
    package_dir={"": "src"}
    packages=find_packages(where="src"),
    include_package_data=True,
    zip_safe=False,
)