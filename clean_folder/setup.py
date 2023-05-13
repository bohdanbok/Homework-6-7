from setuptools import setup

setup(
    name='clean_folder',
    version='1',
    description='Script for cleaning folders',
    url='',
    author='Bohdan Bokariev',
    author_email='b.bokariev@gmail.com',
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:full_sort']}
)