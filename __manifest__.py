# -*- coding: utf-8 -*-
{
    'name': 'Number verify',
    'version': '11.0',
    'category': 'numverify',
    'summary': '',
    'description': """ 
            -Numverify engine using https://apilayer.com/ number verification to check phone number validation on the website checkout
            -Url to get your proper api key after inscription: https://numverify.com/dashboard
                   """,
    'author':  'Ibtissem Zeiri', 
    'depends': ['base','website','website_sale'],
    'data': [  
        'views/config.xml', 
        'views/coheckout.xml', 
             ],
#     'qweb': ['static/src/xml/checkout.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

