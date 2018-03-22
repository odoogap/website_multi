# -*- coding: utf-8 -*-
from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    website_logo = fields.Binary('Logo', attachment=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    footer_description = fields.Text(string='Footer Description')
