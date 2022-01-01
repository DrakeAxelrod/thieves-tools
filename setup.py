from setuptools import setup, find_packages

# pip install --editable .

setup(
    name='thieves-tools',
    author='Drake Axelrod',
    description='Information about useful pen-testing tools in addition to any reusable scripts I myself have written',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['thvtools'],
    python_requires='>=3.10',
    install_requires=[
            'click',
            'beautifulsoup4',
            'pywebview'
    ],
    entry_points={
        'console_scripts': [
            'thvtools=thvtools:cli'
        ]
    }
)
