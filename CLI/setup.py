from setuptools import setup

# To install the CLI, navigate through cmd to this dir, and run this command:
# pip install -e .
# Then you could try

setup(
    name='CLI',
    version='0.1.0',
    packages='search',
    entry_points={
        'console_scripts': [
            'search = search.__main__:main'
        ]
    }
)
