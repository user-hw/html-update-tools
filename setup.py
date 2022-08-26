from setuptools import setup

setup(
    name='html-update',
    version='0.1',
    py_modules=['htmlUpdate','service','common'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        html=htmlUpdate:cli
        
    ''',
)