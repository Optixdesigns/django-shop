from setuptools import setup, find_packages
import os

setup(name='django-shop',
    version='0.0.4',
    description='Django Shop',
    #long_description = read('README.rst'),
    author='Sjoerd Arendsen',
    url='https://github.com/Optixdesigns/django-shop',
    install_requires=('djutils', 'django-polymorphic',),
    packages=find_packages(exclude=["demos", "demos.*"]),
    include_package_data=True,
    zip_safe = False
)