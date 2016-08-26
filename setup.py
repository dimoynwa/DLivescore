from setuptools import setup, find_packages

setup(
    name="DLivescore",
    version="1.0",
    packages=find_packages(),
    install_requires=['requests'],
    description="Football livescore",
    url="https://github.com/dimoynwa/DLivescore",
    license="GNU",
    keywords="livescore",
    author="Dimo Georgiev Drangov",
    author_email="dimodrangov@gmail.com",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
    ],
)
