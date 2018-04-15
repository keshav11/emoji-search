from setuptools import setup
import os

setup(
    name='emojisearch',
    packages=['emojisearch'],
    version='0.2.8',
    description='search emojis using command line',
    keywords='emoji cli command-line search emojisearch emoji-search',
    author='Keshav Gupta',
    author_email='keshav1032@gmail.com',
    license='MIT',
    url='https://github.com/keshav11/emoji-search',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    entry_points={
        'console_scripts': ['emojisearch=emojisearch.emojisearch:main'],
    }
)
