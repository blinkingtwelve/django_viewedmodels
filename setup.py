import os
from setuptools import find_packages, setup

requirements_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements', 'base.txt')


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_viewedmodels',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',  # example license
    description='A Django app to define Postgres Views as Models',
    long_description=read('README.rst'),
    url='https://github.com/joshbrooks/django_viewedmodels/',
    author='Joshua Brooks',
    author_email='josh@catalpa.io',
    install_requires=open(requirements_file_path).read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
