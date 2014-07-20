from distutils.core import setup

setup(
    name='qmachine',
    version='0.0.1',
    author='Sean Wilkinson',
    author_email='sean@qmachine.org',
    packages=['qmachine', 'qmachine.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/qmachine/',
    license='LICENSE.txt',
    description='A platform for World Wide Computing',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
