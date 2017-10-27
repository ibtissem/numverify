# -*- coding: utf-8 -*-
from openerp import models, fields, api, _  
    
class numverify(models.Model): 
    _inherit = "website"   
    
#     api key of numverify.com
    api_numverify = fields.Char('Api Numverify') 
