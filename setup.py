from setuptools import find_packages, setup

setup(
    name='sprocketlib',
    packages=find_packages(include=['sprocketlib']),
    version='0.1.0',
    description='Sprocket Blueprint Loading Library',
    author='FormulaCarbon',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)