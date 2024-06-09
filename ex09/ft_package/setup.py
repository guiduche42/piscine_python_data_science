from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/guiduche42/piscine_python_data_science',
    author='guiduche',
    author_email='guillemette.duchateau@gmail.com',
    license='42',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: 42 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
