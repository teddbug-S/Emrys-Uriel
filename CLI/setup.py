from setuptools import setup

setup(
    name='CLI',
    version='0.7.0',
    packages=['search', 'textspider'],
    entry_points={
        'console_scripts': [
            'search = search.__main__:main',
            'textspider' = textspider.__main__:main',
        ]
    }
)
