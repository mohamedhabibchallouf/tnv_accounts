# -*- coding: utf-8 -*-
from odoo import http

# class TnvAccount(http.Controller):
#     @http.route('/tnv_account/tnv_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tnv_account/tnv_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tnv_account.listing', {
#             'root': '/tnv_account/tnv_account',
#             'objects': http.request.env['tnv_account.tnv_account'].search([]),
#         })

#     @http.route('/tnv_account/tnv_account/objects/<model("tnv_account.tnv_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tnv_account.object', {
#             'object': obj
#         })