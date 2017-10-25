# -*- coding: utf-8 -*-

{
    'name': 'Numverify connector',
    'version': '10.0',
    'category': 'Search',
    'summary': '',
    'description': """

Numverify connector engine
Numverify connector engine using https://apilayer.com/ number verification
Url to get your proper api key after inscription: https://numverify.com/dashboard
==========================


    """,

    'author':  'Ibtissem Zeiri', 

    'depends': ['base','website','website_sale'],

    'data': [  
        'views/config.xml', 
        'views/checkout.xml',
             ],

    'installable': True,
    'auto_install': False,
    'application': False,
}

