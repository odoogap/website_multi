# -*- coding: utf-8 -*-
from odoo import models
from odoo.http import request


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def get_website_contact(self):
        # Get website info for contactus website page
        if request.httprequest.path == '/contactus':
            return request and hasattr(request, 'website') and request.website or False
        return False
