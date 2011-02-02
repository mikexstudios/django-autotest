django-autotest
===============
http://github.com/mikexstudios/django-autotest
by Michael Huynh (mike@mikexstudios.com)

Purpose:
-------

Adds a command to manage.py to automatically run tests whenever project file
changes are detected.

Tested:
------

Django 1.2.x

How to use
----------

1.  Place the directory 'django_fakewall' somewhere in your path. You can do this
    by running setup.py or installing through pip.

2.  Edit settings.py and add `django_autotest` to your `INSTALLED_APPS`.

3.  Run `./manage autotest <args>` from the command line where `<args>` are the
    usual arguments passed to `./manage test <args>`.
