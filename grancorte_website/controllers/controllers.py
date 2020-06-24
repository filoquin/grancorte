# -*- coding: utf-8 -*-
# from odoo import http


# class GrancorteWebsite(http.Controller):
#     @http.route('/grancorte_website/grancorte_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grancorte_website/grancorte_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('grancorte_website.listing', {
#             'root': '/grancorte_website/grancorte_website',
#             'objects': http.request.env['grancorte_website.grancorte_website'].search([]),
#         })

#     @http.route('/grancorte_website/grancorte_website/objects/<model("grancorte_website.grancorte_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grancorte_website.object', {
#             'object': obj
#         })
