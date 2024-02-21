# -*- coding: utf-8 -*-
{
    'name': "Herencia de modulos nativos",

    'summary': """
        Herencia de modulos nativos de Odoo, aumentando campos y metodos a los productos""",

    'description': """
        R1: Agregar un nuevo campo a los productos de Odoo
        R1.1: Realizar una herencia al modulo product.template y agregar un nuevo campo "Talla" de tipo Char 
        R1.2: Realizar una herencia al modulo product.template y agregar un nuevo campo "Marca" de tipo Many2one
        R1.3: Agregar un nuevo método al modulo product.template que lance un al presionarlo
        R1.4 Herencia de Vista (form, tree): Agregar los campos en la vista form y tree
    """,

    'author': "Nicole Durand Zeballos",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
