from datetime import date
from odoo import models, fields, api


class persona(models.Model):
    _name = 'campos_relacionales.persona'
    _description = 'campos_relacionales.persona'

    name = fields.Char()
    birth_date = fields.Date()
    age = fields.Integer(compute='_compute_age', string='Age')
    
    pareja = fields.Many2one(
        'campos_relacionales.persona', 
        string='Pareja'
    )
    amigos = fields.Many2many(
        'campos_relacionales.persona',
        'relacion_amigos', 
        'persona_id', 
        'amigo_id', 
        string='Amigos'
    )
    
    hijos = fields.One2many(
        'campos_relacionales.persona',
        'padre_id', 
        string='Hijos'
    )

    padre_id = fields.Many2one(
        'campos_relacionales.persona',
        string='Padre'
    )
    
    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for persona in self:
            if persona.birth_date:
                birth_date = fields.Date.from_string(persona.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                persona.age = age
            else:
                persona.age = 0
