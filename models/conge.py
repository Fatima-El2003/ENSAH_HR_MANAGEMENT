from odoo import models, fields

class EnsahConge(models.Model):
    _name = 'ensah.conge'
    _description = 'Gestion des Congés'

    # Champs de la classe EnsahConge
    id_conge = fields.Integer('ID Congé', required=True)
    date_debut = fields.Date('Date de Début', required=True)
    date_fin = fields.Date('Date de Fin', required=True)
    nature = fields.Char('Nature du Congé', required=True)
    commentaire = fields.Text('Commentaire')

    # Relation Many2one avec EnsahEmployee
    employee_id = fields.Many2one('ensah.employee', string='Employé', required=True)
