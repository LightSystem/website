#!/bin/bash

python3 odoo/odoo-bin \
  --db_host "localhost" -r "odoo" -w "odoo" \
  --http-interface 127.0.0.1 \
  --addons-path odoo/addons \
  -D data \
  -d website_odoo \
  -i TBD \
  -u all
