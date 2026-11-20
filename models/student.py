from odoo import models,fields

class Student(models.Model):
    _name = 'college.student'
    _description = 'College Student'

    name = fields.Char(string='Student Name',required=True)
    enrollment_no = fields.Char(string='Enrollment Number',required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone number')
    gender = fields.Selection(
        [
            ('male','Male'),
            ('female','Female'),
            ('other','Other')
        ],
        string='Gender'
    )
    dob = fields.Date(string='Date of Birth')
    course = fields.Char(string='Course')
    admission_date = fields.Date(string='Admission Date',default=fields.Date.today)
    address = fields.Text(string='Address')
    active = fields.Boolean(string='Active',default=True)