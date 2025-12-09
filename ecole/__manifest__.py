{
    'name': "Ecole",

    'summary': "Application pour la gestion des étudiants de la filière MGSI",

    'description': """Cette application vous permet de gérer tous les étudiants de la filière MGSI""",

    'author': "Hanae Boudabza",
    'website': "http://ensao.ump.ma/fr",

    'application': True,
    'license': 'LGPL-3',
    'sequence':-1,
    'auto-update': True,
    'installable': True,

    'category': 'Uncategorized',
    'version': '19.0.1.0',


    'depends': ['base','web'],

    'data': [
        'security/ir.model.access.csv',
        'views/etudiant_view.xml',
        'views/filiere_view.xml',
        'views/module_view.xml',  
        'views/salle_view.xml',   
        'views/menus.xml',        
    ],
}

