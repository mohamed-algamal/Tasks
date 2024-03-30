# -*- coding: utf-8 -*-
{
    'name': "task management",
    'summary': "this for me for make tasks",
    'description': """
    """,
    'author': "Mohamed Algamal",
    'category': 'task',
    'version': '1.0.0',
    'depends': ['base','mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/task_one_view.xml',
        'views/task_two_view.xml',
    ],
    'demo': [],
    'excludes': [''],
    'sequence': -100,
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
