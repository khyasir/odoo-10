# -*- coding: utf-8 -*-
{
    'name': "V4 Performa Invoice",

    'summary': "V4 Performa Invoice",

    'description': "V4 Performa Invoice",

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
