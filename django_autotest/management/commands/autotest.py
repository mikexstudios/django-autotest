from django.core.management.base import BaseCommand, CommandError
from django.utils import autoreload

from subprocess import Popen
import sys

class Command(BaseCommand):
    args = '<testargs>'
    help = 'Automatically runs tests when files have changed. <testargs> accept' +\
           'same arguments for test.'

    def handle(self, *args, **options):
        autoreload.main(self.run, args, options)

    def run(self, *args, **options):
        #Convert args and options to string.
        #PROBLEM: Somehow django inserts a bunch of options in here like:
        #         --pythonpath=None --verbosity=1 --traceback=None --settings=None
        #         which messes up the arguments to 'test'.
        #testargs = ' '.join(['--%s=%s' % (k,v) for (k,v) in options.iteritems()])
        #testargs += ' '
        testargs = ' '.join(map(str, args))
        
        Popen('python manage.py test %s' % testargs, stdout=sys.stdout, stderr=sys.stderr,
                shell=True, bufsize=0, close_fds=True)

