#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/hsfolkes.github.io/")

from app import app as application
application.secret_key = 'spring17project5'
