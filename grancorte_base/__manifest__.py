# -*- coding: utf-8 -*-
{
    'name': "grancorte",

    'summary': """
        Modulo de implemetacion base de Gran corte""",

    'description': """
        Gran corte
        Modulo de implementacion de frigorifico gran corte
    """,

    'author': "Filoquin",
    'website': "http://www.sipecu.com.ar",
    'category': 'base',
    'version': '13.0.1.0.1',
    'depends': [
        'stock',
        'l10n_ar',
        'website_sale',
        'theme_grancorte'
    ],

    'data': [
        # 'security/ir.model.access.csv',
        'data/res_company.xml',
        #'data/website.xml',
        'data/products.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
