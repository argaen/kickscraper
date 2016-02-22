import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='kickscraper',
    version='0.1.0',
    description='A scraper for Crowdfunding projects',
    long_description=long_description,
    url='https://github.com/argaen/kickscraper',

    author='argaen',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
    ],

    keywords='kickstarter api crowdfunding projects',

    packages=['kickscraper'],

    install_requires=['requests>=2.9.1', 'beautifulsoup>=4.4.1'],
)
