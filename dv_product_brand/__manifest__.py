# -*- coding: utf-8 -*-
{
    'name': "Branded product",

    'summary': """
        It inherits from the product template module and adds fields such as brand and size, and adds functionalities.""",

    'description': """
        Long description of module's purpose
    """,

    'author': 'Develogers',
	'website': 'https://develogers.com',
	'support': 'especialistas@develogers.com',
	'live_test_url': 'https://wa.link/2cc9dn',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product'],

    # always loaded
    'data': [
        'views/product_template_views.xml',
    ],
    
    # only loaded in demonstration mode
    'application': False,
    'installable': True,
    'auto_install': True,
}
