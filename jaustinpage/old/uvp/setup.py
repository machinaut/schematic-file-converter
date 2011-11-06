from distutils.core import setup

setup(
    name='uvp',
    version='0.1.0',
    author='Austin Page',
    author_email='jaustinpage@gmail.com',
    packages=['uvp', 'uvp.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://',
    license='LICENSE.txt',
    description='Creates uvp files.',
    long_description=open('README.txt').read(),
    install_requires=[
        "ABrain >= 1.1.1",
        "Athought == 0.1.4",
    ],
)
