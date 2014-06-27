from setuptools import setup, find_packages
import os
import pycharm_debug_middleware

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Gabe Jackson",
    author_email="gabejackson@cxg.ch",
    name='django-pycharm-debug-middleware',
    version=pycharm_debug_middleware.__version__,
    description="A django middleware to debug exceptions in PyCharm's PyDev debugger",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url = 'https://github.com/gabejackson/django-pycharm-debug-middleware',
    license='MIT License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.2',
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    zip_safe = False,
)
