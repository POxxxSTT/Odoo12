# -*- coding: utf-8 -*-
{
    'name': "Zhigailov",
    'summary': "Модуль для учёта персонала",
    'author': "Жигайлов",
    'website': "http://www.yourcompany.com",
    'category': 'Моё',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],

    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}