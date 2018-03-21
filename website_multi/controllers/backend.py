# -*- coding: utf-8 -*-
import odoo
import urllib.parse as urlparse
from odoo import http
from odoo.http import request


class WebsiteBackend(odoo.addons.website.controllers.backend.WebsiteBackend):
    @http.route('/website/fetch_dashboard_data', type='json', auth='user')
    def fetch_dashboard_data(self, date_from, date_to):
        dashboard_data = super(WebsiteBackend, self).fetch_dashboard_data(date_from, date_to)

        try:
            # Get the website Google Analytics key and client id
            website_domain = request.httprequest.headers.get('Referer', False)
            domain = urlparse.urlsplit(website_domain)[1].split(':')[0]

            website = self.env['website'].sudo().search([('domain', 'ilike', domain)], limit=1)
            if website:
                # Replaces Google Analytics metadata
                dashboard_data['dashboards']['visits']['ga_analytics_key'] = website.google_analytics_key
                dashboard_data['dashboards']['visits']['ga_client_id'] = website.google_management_client_id
        except:
            pass

        return dashboard_data
