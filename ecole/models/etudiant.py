from odoo import models, fields

class Etudiant(models.Model):
    _name = 'ecole.etudiant'
    _description = 'Modèle pour la gestion des étudiants'
    NumApogee = fields.Integer(string="Numéro Apogée")
    Nom = fields.Char(string="Nom", required=True)
    Prenom = fields.Char(string="Prénom", required=True)
    Email = fields.Char(string="Email")
    Tel = fields.Integer(string="Téléphone")
    villes = [
        # Oriental
        ('oujda', "Oujda"),
        ('nador', "Nador"),
        ('berkane', "Berkane"),
        ('taourirt', "Taourirt"),
        ('jerada', "Jerada"),
        ('figuig', "Figuig"),

        # Major Cities
        ('casablanca', "Casablanca"),
        ('rabat', "Rabat"),
        ('marrakech', "Marrakech"),
        ('agadir', "Agadir"),
        ('tanger', "Tanger"),
        ('fes', "Fès"),
        ('meknes', "Meknès"),

        # North / Rif
        ('tetouan', "Tétouan"),
        ('alhoceima', "Al Hoceïma"),
        ('chefchaouen', "Chefchaouen"),
        ('larache', "Larache"),

        # Center / Atlas
        ('kenitra', "Kénitra"),
        ('sale', "Salé"),
        ('temara', "Témara"),
        ('mohammedia', "Mohammedia"),
        ('eljadida', "El Jadida"),
        ('beni_mellal', "Béni Mellal"),
        ('khenifra', "Khénifra"),
        ('settat', "Settat"),
        ('khouribga', "Khouribga"),
        ('errachidia', "Errachidia"),
        ('ouarzazate', "Ouarzazate"),

        # South
        ('safi', "Safi"),
        ('essaouira', "Essaouira"),
        ('guelmim', "Guelmim"),
        ('tan_tan', "Tan-Tan"),
        ('laayoune', "Laâyoune"),
        ('dakhla', "Dakhla"),
        ('tarfaya', "Tarfaya"),
    ]
    Ville = fields.Selection(selection=villes, string="Ville", default='oujda')
    Image = fields.Binary(string='Photo'    )
    filiere_id = fields.Many2one(
        comodel_name='ecole.filiere',
        string='Filière'
    )
