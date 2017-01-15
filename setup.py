from setuptools import setup

with open('README.md', 'r') as readme:
    README_TEXT = readme.read()

setup(
    name='kickscraper',
    version='0.1.6',
    description='A scraper for Crowdfunding platform projects like kickstarter',
    long_description=README_TEXT,
    url='https://github.com/argaen/kickscraper',
    author='Manuel Miranda',
    author_email="manu.mirandad@gmail.com",
    license='MIT',
    keywords=['kickstarter api crowdfunding projects'],
    packages=['kickscraper'],
    install_requires=[
        'requests>=2.9.1',
        'beautifulsoup4>=4.4.1'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],

)
