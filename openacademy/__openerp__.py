# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        My first module during training V9""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo - Thibault Francois",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/partner.xml',
        'views/courses.xml',
        'views/sessions.xml',
        'views/partners.xml',
        'views/courses_kanban.xml',
        'wizard/add_attendee_view.xml',
        'report/session.xml',
        'report/board.xml',
        'data/session_workflow.xml',
        'data/partner.xml',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}