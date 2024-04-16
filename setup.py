from setuptools import find_packages, setup

setup(
    name='explore',
    version='0.1',
    description='microservices for exploring open ai',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
