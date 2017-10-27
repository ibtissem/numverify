# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields

class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #Api key of numverify.com 
    api_numverify = fields.Char(related='website_id.api_numverify') 
    
    @api.model
    def get_values(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res = super(WebsiteConfigSettings, self).get_values()  
        website = self.env['website'].search([])
        if website:
            res.update(
                api_numverify = website[0].api_numverify,
            )
        return res
    
    def set_values(self):
        super(WebsiteConfigSettings, self).set_values() 
        set_param = self.env['ir.config_parameter'].sudo().set_param
        website = self.env['website'].search([])
        for wbs in website:
            wbs.write({'api_numverify': self.api_numverify})
    
