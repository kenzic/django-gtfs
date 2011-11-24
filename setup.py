from distutils.core import setup
#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


class mytest(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()

setup(
    name = "django-gtfs",
    packages = ["gtfs", "gtfs.migrations", "gtfs.management"],
    package_data={'gtfs': ['fixtures/initial_data.json']},
    version = "0.0.1",
    description = "Django application to load/dump and more generally handle GTFS transit data specification",
    author = "Olivier Girardot",
    author_email = "ssaboum@gmail.com",
    url = "https://github.com/ssaboum/django-gtfs",
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
