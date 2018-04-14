from setuptools import setup

setup(
    name='emojisearch',
    packages=['emojisearch'],
    version='0.0.1',
    author='Keshav Gupta',
    license='MIT',
    entry_points={
        'console_scripts': ['emojisearch=emojisearch.emojisearch:main'],
    }
)
