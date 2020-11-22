from setuptools import setup

setup(
    name='CLI',
    version='0.4.0',
    packages=['search'],
    entry_points={
        'console_scripts': [
            'search = search.__main__:main',
        ]
    }
)
