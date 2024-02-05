from odoo import models, fields, api


class subject(models.Model):
    _name = 'school.subject'
    _description = 'school.subject'

    name = fields.Char()
    credits = fields.Integer()
    max_students = fields.Integer()
    active = fields.Boolean()
    teacher_id = fields.Many2one(
        'school.teacher', string='Teacher'
    )
    student_ids = fields.Many2many(
        'school.student', string='Students'
    )





