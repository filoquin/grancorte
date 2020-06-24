# -*- coding: utf-8 -*-
# from odoo import http


# class GrancorteBase(http.Controller):
#     @http.route('/grancorte_base/grancorte_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grancorte_base/grancorte_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('grancorte_base.listing', {
#             'root': '/grancorte_base/grancorte_base',
#             'objects': http.request.env['grancorte_base.grancorte_base'].search([]),
#         })

#     @http.route('/grancorte_base/grancorte_base/objects/<model("grancorte_base.grancorte_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grancorte_base.object', {
#             'object': obj
#         })
