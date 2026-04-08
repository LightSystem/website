# -*- coding: utf-8 -*-
{
    'name': 'lightsystem Website',
    'summary': 'Freelancer website foundation built on Odoo Website',
    'author': 'João Horta Alves',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/lightsystem_website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'lightsystem_website/static/src/scss/lightsystem_website.scss',
        ],
    },
    'installable': True,
    'application': False,
}
