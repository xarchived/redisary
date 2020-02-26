import re

from setuptools import setup

with open('redisary/__init__.py') as f:
    version = re.search(r'([0-9]+(\.dev|\.|)){3}', f.read()).group(0)

with open('README.md') as f:
    readme = f.read()

name = 'redisary'
owner = 'xurvan'

setup(
    name=name,
    version=version,
    license='apache-2.0',
    description='Redis as dictionary',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Xurvan',
    url=f'https://github.com/{owner}/{name}',
    download_url=f'https://github.com/{owner}/{name}/archive/v{version}.zip',
    project_urls={
        'Code': f'https://github.com/{owner}/{name}',
        'Issue tracker': f'https://github.com/{owner}/{name}/issues',
    },
    packages=[name],
    install_requires=['redis'],
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
)
