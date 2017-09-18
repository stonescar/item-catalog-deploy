activate_this = '/var/www/itemCatalog/catalog/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
from catalog import app as application


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/itemCatalog/")

application.secret_key = 'items'
