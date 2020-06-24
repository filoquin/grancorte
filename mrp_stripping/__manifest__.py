# -*- coding: utf-8 -*-
{
    'name': "mrp stripping",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "filoquin",
    'website': "http://www.sipecu.com.ar",
    'category': 'Manufacturing',
    'version': '13.0.1.0.1',
    'depends': ['mrp'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_bom_views.xml',
    ],
}
