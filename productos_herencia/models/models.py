# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'

    talla = fields.Char(string="Talla")
    marca = fields.Many2one('product.brand', string="Marca")
    
    