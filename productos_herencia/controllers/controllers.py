# -*- coding: utf-8 -*-
# from odoo import http


# class ProductosHerencia(http.Controller):
#     @http.route('/productos_herencia/productos_herencia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/productos_herencia/productos_herencia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('productos_herencia.listing', {
#             'root': '/productos_herencia/productos_herencia',
#             'objects': http.request.env['productos_herencia.productos_herencia'].search([]),
#         })

#     @http.route('/productos_herencia/productos_herencia/objects/<model("productos_herencia.productos_herencia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('productos_herencia.object', {
#             'object': obj
#         })
