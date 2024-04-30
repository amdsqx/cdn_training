from odoo import models, fields, api


# omod shortcut untuk class model
# class model respartner dan untuk mengambil data respartner dengan inherit
class ResPartner(models.Model):
    _inherit = 'res.partner'

    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),])
    
    provinsi_id = fields.Many2one(comodel_name='ref.provinsi', string='Provinsi')
    kota_id = fields.Many2one(comodel_name='ref.kota', string='Kota')
    kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Kecamatan')
    desa_id = fields.Many2one(comodel_name='ref.desa', string='Desa')
    
