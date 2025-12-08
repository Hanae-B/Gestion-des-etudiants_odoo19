# from odoo import models, fields, api


# class ecole(models.Model):
#     _name = 'ecole.ecole'
#     _description = 'ecole.ecole'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

