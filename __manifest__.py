{
    'name':'College Management',
    'version':'1.0.0',
    'summary':'College Management System',
    'category':'Education',
    'depends':['base'],
    'data':[
        'security/ir.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}