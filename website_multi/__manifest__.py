# -*- coding: utf-8 -*-
{
    'name': 'Multi Website',
    'version': '11.0.0.1',
    'author': 'Odoo Gap',
    'summary': 'Set up Multi-Websites, Multi-Theme, Multi-eCommerce, Multi-Company on a single database',
    'description': """
Multi Website
=============
Set up Multi-Websites, Multi-Theme, Multi-eCommerce, Multi-Company on a single database.""",
    'website': 'https://www.odoogap.com',
    'category': 'Website',
    'depends': [
        'website_multi_theme',
    ],
    'data': [
        'views/website_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
