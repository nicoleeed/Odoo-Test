from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.template'
    
    size = fields.Char(string='Talla')
    brand = fields.Many2one('product.brand', string='Marca')
    
    def raise_error(self):
        raise ValueError("¡Este botón genera un error intencionalmente!")