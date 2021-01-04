from setuptools import setup

with open('README.md', 'r') as rd:
    long_description = rd.read()

setup(
    name='medianizer',
    version='0.0.1',
    description='Medianizer - media files organizer',
    long_description=long_description,
    author='Maxim Babushkin',
    packages=['medianizer'],
    install_requires=['ExifRead>=2.3.2'],
    python_requires='>3.0.0',
    entry_points={
        'console_scripts': [
            'medianizer = medianizer.executor:main',
        ]
    }
)
