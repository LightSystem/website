# -*- coding: utf-8 -*-
{
    'name': 'lightsystem Website',
    'author': 'João Horta Alves',
    'license': 'LGPL-3',
    'depends': ['website'],
    'installable': True,
    'application': False,
    'assets': {
        'web._assets_primary_variables': [
            'lightsystem_website/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'lightsystem_website/static/src/scss/bootstrap_overridden.scss'),
        ],
        # theme.scss contains compiled CSS rules and loads after Bootstrap.
        'web.assets_frontend': [
            'lightsystem_website/static/src/scss/theme.scss',
        ],
    },
}
