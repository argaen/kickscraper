from setuptools import setup


setup(
    name='kickscraper',
    version='0.1.3',
    description='A scraper for Crowdfunding projects',
    url='https://github.com/argaen/kickscraper',

    author='argaen',
    license='MIT',

    keywords=['kickstarter api crowdfunding projects'],

    packages=['kickscraper'],

    install_requires=['requests>=2.9.1', 'beautifulsoup4>=4.4.1'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],

)
