from odoo import models, fields,exceptions, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'

    name = fields.Char(string="Type Name", required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', string="Properties")
    sequence = fields.Integer('Sequence', default=1)
    #property_ids = fields.Many2one('estate.property', string="Properties")
    # property_type_id = fields.Char(string="Property Type", required=True)
    # buyer_id = fields.Many2one('estate.property', string="Buyer")
    # seller_id = fields.Many2one('estate.property', string="Seller")

    #SQL constraint
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The property type name must be unique.')
    ]
    #model Ordering
    _order = 'name asc'
    # @api.constrains('name')
    # def _check_unique_name(self):
    #     for record in self:
    #         existing_type = self.search([('name', '=', record.name), ('id', '!=', record.id)])
    #         if existing_type:
    #             raise exceptions.ValidationError("The property type name must be unique.")
