from setuptools import setup

setup(
    name='CLI',
    version='0.2.0',
    packages=['search', 'searchword'],
    entry_points={
        'console_scripts': [
            'search = search.__main__:main',
            'searchword = searchword.__main__:main'
        ]
    }
)
