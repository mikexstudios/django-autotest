from django.core.management.base import BaseCommand, CommandError
from django.utils import autoreload

from subprocess import Popen
import sys

class Command(BaseCommand):
    args = '<app>'
    help = 'Automatically runs tests on <app> when files have changed.'

    def handle(self, *args, **options):
        #TODO: Validate arguments
        #try:
        #    app = args[0]
        #except IndexError:
        #    raise CommandError('<app> argument not specified!')

        autoreload.main(self.run, args, options)

    def run(self, *args, **options):
        Popen('./manage.py test %s' % args[0], stdout=sys.stdout, stderr=sys.stderr,
                shell=True, bufsize=0, close_fds=True)

