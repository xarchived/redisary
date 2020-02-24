from setuptools import setup
import re

with open('redict/__init__.py') as f:
    version = re.search(r'([0-9]+(\.|-dev|)){3}', f.read()).group(0)

setup(
    name='redict',
    version=version,
    description='Redis as dictionary',
    author='Xurvan',
    packages=['redict'],
    install_requires=['redis'],
    python_requires='>=3.6',
    zip_safe=False)
