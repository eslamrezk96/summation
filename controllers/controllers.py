# -*- coding: utf-8 -*-
from odoo import http

# class Summation(http.Controller):
#     @http.route('/summation/summation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/summation/summation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('summation.listing', {
#             'root': '/summation/summation',
#             'objects': http.request.env['summation.summation'].search([]),
#         })

#     @http.route('/summation/summation/objects/<model("summation.summation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('summation.object', {
#             'object': obj
#         })