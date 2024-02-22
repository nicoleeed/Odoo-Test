from odoo import api, fields, models, _


class ProductBrand(models.Model):
	_name = 'product.brand'
	_description = 'Product Brand'

	name = fields.Char(string='Marca')