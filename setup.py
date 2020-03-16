__version__ = '2.0.0'

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(name='robogerctl',
                 version=__version__,
                 author='Altertech',
                 author_email='pr@altertech.com',
                 description='Roboger CLI tool and management library',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/alttch/robogerctl',
                 packages=setuptools.find_packages(),
                 license='Apache License 2.0',
                 install_requires=[
                     'requests',
                     'pyyaml',
                     'rapidtables',
                     'neotermcolor',
                 ],
                 classifiers=(
                     'Programming Language :: Python :: 3',
                     'License :: OSI Approved :: Apache Software License',
                     'Topic :: Communications',
                 ),
                 scripts=['bin/robogerctl'])
