#!/usr/bin/env python

import os, sys
if __name__ == "__main__":
	sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demoshop.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)