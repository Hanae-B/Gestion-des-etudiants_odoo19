from odoo import models, fields


class Salle(models.Model):
    _name = 'ecole.salle'
    _description = 'Salle'

    # CRITICAL: This ensures dropdowns show "Salle 1" instead of "ecole.salle,1"
    _rec_name = 'salle'

    code = fields.Char(string="Code", required=True)
    salle = fields.Char(string="Nom de la Salle", required=True)
    bloc = fields.Char(string="Bloc")