# -*- coding: utf-8 -*-
from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    website_logo = fields.Binary('Logo', attachment=True)
    footer_company_name = fields.Char(string='Company Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    footer_description = fields.Text(string='Description')
    website_styles = fields.Text(string='CSS')
