from setuptools import setup, find_packages

setup(
    name='ds_forge',
    version='0.0.1',
    author='Harisiva R G',
    author_email='harisivarg@gmail.com',
    description='A package to create a data science project structure',
    long_description=open('README.md').read(),
    url='https://github.com/Harisiva-rg/ds_forge',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['logging'], 
    entry_points={
        'console_scripts': [
            'template=template:main',
        ],
    },
)
