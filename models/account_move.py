from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    external_origin = fields.Char(
        string = 'externe Re-Nr.',
        help='Re-Nr des Lieferanten',
        store=True,
        readonly=False,)
