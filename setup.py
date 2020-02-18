from setuptools import setup, find_namespace_packages

version = '0.1.0'

setup(
    name='ODP-API-ElasticAdapter',
    version=version,
    description='Elastic search agent adapter for the ODP API',
    url='https://github.com/SAEONData/ODP-API-ElasticAdapter',
    author='Mark Jacobson',
    author_email='mark@saeon.ac.za',
    license='MIT',
    packages=find_namespace_packages(),
    python_requires='~=3.6',
    install_requires=[
        'requests',
    ],
    extras_require={
        'test': ['pytest', 'coverage']
    },
)