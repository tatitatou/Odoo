# -*- coding: utf-8 -*-
{
    'name': "Location de véhicules",

    'summary': "Outils de gestion de véhicules",

    'description': """
Outils de gestion de véhicules
    """,

    'author': "Tatiana Novion",
    'website': "https://www.rentcarsTN.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/cars',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True,
    'license': "AGPL-3",
    'images': [
       'static/description/icon.png',
    ],


    # always loaded
    'data': [
        'security/rentcars_security.xml',
        'security/ir.model.access.csv',
        'views/rentcars_menu.xml',
        'views/vehicle_views.xml' 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

