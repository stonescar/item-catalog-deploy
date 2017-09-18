#!/usr/bin/env python
# -*- coding: utf-8 -*-
from catalog.modules.setup.app import app


if __name__ == '__main__':
    app.secret_key = 'items'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
