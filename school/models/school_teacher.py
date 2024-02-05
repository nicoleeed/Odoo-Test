from odoo import models, fields, api

class school_teacher(models.Model):
    _name = 'school.teacher'
    _description = 'school.teacher'

    name = fields.Char()
    profile = fields.Text()

    subject_ids = fields.One2many(
        'school.subject', 'teacher_id', string='Subjects')
