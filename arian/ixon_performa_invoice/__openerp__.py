# -*- coding: utf-8 -*-
{
    'name': "Ixon Proforma Invoice",

    'summary': "Ixon Proforma Invoice",

    'description': "Ixon Proforma Invoice",

    'author': "Muhammmad Kamran",
    'website': "http://www.bcube.com",

    # any module necessary for this one to work correctly
    'depends': ['base', 'report','sale'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
