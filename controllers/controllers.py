# -*- coding: utf-8 -*-
# from odoo import http


# class OdooBasico(http.Controller):
#     @http.route('/odoo_basico/odoo_basico', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_basico/odoo_basico/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_basico.listing', {
#             'root': '/odoo_basico/odoo_basico',
#             'objects': http.request.env['odoo_basico.odoo_basico'].search([]),
#         })

#     @http.route('/odoo_basico/odoo_basico/objects/<model("odoo_basico.odoo_basico"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_basico.object', {
#             'object': obj
#         })

