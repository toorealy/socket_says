from setuptools import find_packages, setup


setup(
    name='SocketSays',
    version='0.1.1',
    description='Easy socket conversations',
    license='LICENSE',
    packages=find_packages(),
    install_requires=[
        'ipaddress',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
