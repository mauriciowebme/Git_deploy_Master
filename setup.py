from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='comandos_pycmd',
    version='0.0.1',
    packages=['pycmd_pack'],
    description='API de comandos facilitados cmd',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/mauriciowebme/comandos_pycmd.git',
    author='Mauricio Azeredo',
    license='MIT',
    author_email='mauriciowebme@gmail.com',
    install_requires=[
        'requests'
    ]
)#