from datetime import date

from odoo import models, fields, api


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char()
    birth_date = fields.Date()
    final_exam_grade = fields.Float()

    subject_ids = fields.Many2many(
        'school.subject', string='Subjects'
    )

    age = fields.Integer(compute='_compute_age', string='Age')

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for student in self:
            if student.birth_date:
                birth_date = fields.Date.from_string(student.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                student.age = age
            else:
                student.age = 0

