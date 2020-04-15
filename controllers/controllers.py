# -*- coding: utf-8 -*-
# from odoo import http


# class CitcomNpwp(http.Controller):
#     @http.route('/citcom_npwp/citcom_npwp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citcom_npwp/citcom_npwp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citcom_npwp.listing', {
#             'root': '/citcom_npwp/citcom_npwp',
#             'objects': http.request.env['citcom_npwp.citcom_npwp'].search([]),
#         })

#     @http.route('/citcom_npwp/citcom_npwp/objects/<model("citcom_npwp.citcom_npwp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citcom_npwp.object', {
#             'object': obj
#         })
