#!/usr/bin/env python
from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings')
except ImportError:
    import sys
    sys.stderr.write(
        "Error: Can't find the file 'settings.py'" \
        " in the directory containing %r." \
        " It appears you've customized things.\n" \
        " You'll have to run django-admin.py," \
        " passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    import os
    try:
        os.makedirs(settings.SKETCHES_DIR)
    except:
        pass        
    execute_manager(settings)
