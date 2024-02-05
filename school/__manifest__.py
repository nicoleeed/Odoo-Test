# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': "Module that represents the basic characteristics of a school",

    'description': """
    The School module represents the teachers of a school, their relationship with the courses taught, and also the students, as well as their relationship with the courses.
    """,

    'author': "Nicole Durand Zeballos",
    'website': "www.linkedin.com/in/nicole-alexia-durand-zeballos-46b231284",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/school_teacher_view.xml',
        'views/school_student_view.xml',
        'views/school_subject_view.xml',
        'views/menu_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

