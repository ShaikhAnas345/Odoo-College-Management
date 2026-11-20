from odoo import models,fields

class Course(models.Model):
    _name = 'college.course'
    _description = 'College Course'

    name = fields.Char(string='Course Name',required=True)
    code = fields.Char(string='Course Code',required=True)
    duration = fields.Char(string='Duration')
    fees = fields.Float(string='Course Fees')
    department = fields.Char(string='Department')
    description = fields.Text(string='Course Description')
    active = fields.Boolean(string='Active',default=True)