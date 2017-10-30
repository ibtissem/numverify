# -*- coding: utf-8 -*-

{
    'name': 'Number verify',
    'category': 'numverify',
    'version': '1.0',
    'summary': '',
    'description': """ 
            -Numverify engine using https://apilayer.com/ number verification to check phone number validation on the website checkout
            -Url to get your proper api key after inscription: https://numverify.com/dashboard
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

