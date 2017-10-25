# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    #Api key of numverify.com 
    api_numverify = fields.Char(related='website_id.api_numverify') 
    
    @api.model
    def get_default_api_numverify(self, fields):
        website_obj = self.env['website']
        website = website_obj.search([])
        if website:
            return {'api_numverify': website[0].api_numverify }
 
    @api.multi
    def set_api_numverify(self):
        website_obj = self.env['website']
        for record in self:
            website = website_obj.search([])
            numm = record.api_numverify
            if website:
                for wbs in website:
                    wbs.write({'api_numverify': record.api_numverify })
        return True