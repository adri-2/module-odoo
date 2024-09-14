# -*- coding: utf-8 -*-
# from odoo import http


# class Link-code-qr(http.Controller):
#     @http.route('/link-code-qr/link-code-qr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/link-code-qr/link-code-qr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('link-code-qr.listing', {
#             'root': '/link-code-qr/link-code-qr',
#             'objects': http.request.env['link-code-qr.link-code-qr'].search([]),
#         })

#     @http.route('/link-code-qr/link-code-qr/objects/<model("link-code-qr.link-code-qr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('link-code-qr.object', {
#             'object': obj
#         })
