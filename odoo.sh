#!/bin/bash

python3 odoo/odoo-bin \
  --db_host "localhost" -r "odoo" -w "odoo" \
  --http-interface 127.0.0.1 \
  --addons-path odoo/addons,lightsystem-addons \
  -D data \
  -d lightsystem_website_odoo19 \
  -i lightsystem_website \
  -u all
