from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Timelog tracker'
LONG_DESCRIPTION = 'Measures time between events and collects events in between'

# Setting up
setup(
        name="timelog", 
        version=VERSION,
        author="WolffParkinson",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            "humanize >= 3.12.0",
            "six",
        ],
        
        keywords=['python', 'timelog', 'time'],
        license='MIT',
        classifiers= [
            "Development Status :: 2 - Pre-Alpha",
            'Intended Audience :: Developers',
            "Operating System :: Microsoft :: Windows",
            'Topic :: Database',
            'Programming Language :: Python :: 3.9',
        ]
)