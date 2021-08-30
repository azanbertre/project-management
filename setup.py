from setuptools import setup, find_packages


setup(
    name='app',
    version='0.0.1',
    description='',
    author='Various',
    url='https://github.com/azanbertre/project-management',
    install_requires=[
        'flask',
        'pymongo',
        'bcrypt',
        'werkzeug',
        'pytest',
        'apscheduler',
        'fire'
    ],
    packages=find_packages()
)
