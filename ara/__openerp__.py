# -*- coding: utf-8 -*-
{
    'name': "ara",

    'summary': """Austrian Recyling Association""",

    'description': """
	Add or modify product recyling methods.
    """,

    'author': "Md. Meftaul Haque Mishu",
    'website': "http://3spire.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
	'views/ara.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
