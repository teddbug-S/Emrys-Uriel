from setuptools import setup

setup(
    name='CLI',
    version='0.2.0',
    packages=['search', 'wordsearch'],
    entry_points={
        'console_scripts': [
            'search = search.__main__:main',
            'wordsearch = wordsearch.__main__:main'
        ]
    }
)
