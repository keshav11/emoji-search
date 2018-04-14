from setuptools import setup
import os

setup(
    name='emojisearch',
    packages=['emojisearch'],
    version='0.2.2',
    description='search emojis using command line',
    keywords='emoji search emojisearch emoji-search',
    author='Keshav Gupta',
    author_emao='keshav1032@gmail.com',
    license='MIT',
    url='https://pypi.org/project/emojisearch/',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['emojisearch=emojisearch.emojisearch:main'],
    }
)
