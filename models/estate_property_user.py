from odoo import models, fields, api

class EstatePropertyUser(models.Model):
    _inherit = 'estate.property'

    user_id = fields.Many2one(
        'res.users', 
        string='Responsible User', 
        default=lambda self: self.env.user,
        help='The user responsible for this property.'
    )
    property_ids = fields.One2many(
        'estate.property', 'user_id', string='Properties',
        help='List of properties managed by this user.'
    )