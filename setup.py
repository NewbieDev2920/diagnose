from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.1',
    packages=find_packages(where='src'),  # Look for packages in src directory
    package_dir={'': 'src'},              # Tell setuptools that packages are under src
    python_requires='>=3.6',
)