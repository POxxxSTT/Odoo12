# -*- coding: utf-8 -*-
from odoo import http

# class Zhigailov(http.Controller):
#     @http.route('/zhigailov/zhigailov/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zhigailov/zhigailov/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zhigailov.listing', {
#             'root': '/zhigailov/zhigailov',
#             'objects': http.request.env['zhigailov.zhigailov'].search([]),
#         })

#     @http.route('/zhigailov/zhigailov/objects/<model("zhigailov.zhigailov"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zhigailov.object', {
#             'object': obj
#         })