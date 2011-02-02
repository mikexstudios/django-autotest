from setuptools import setup, find_packages

setup(
    name = 'django_autotest',
    packages = find_packages(),
    version = '1.0.0',
    description = 'Adds a command to manage.py to automatically run tests whenever project file changes are detected.',
    author = 'Michael Huynh',
    author_email = 'mike@mikexstudios.com',
    url = 'http://github.com/mikexstudios/django-autotest',
    classifiers=[
        'Programming Language :: Python', 
        'Framework :: Django', 
        'License :: OSI Approved :: BSD License',
    ]
)

