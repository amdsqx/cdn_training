from odoo import models, fields, api

class Peserta(models.Model):
    _name = 'peserta'
    _description = 'Peserta'
    _inherits = {'res.partner':'partner_id'}

    # extrak partner_id dari inherits res.partner,m2o artinya data banyak diambil sebagian, string 'Partner ID' judul, required=True artinya jika tidak diisi maka error, ondelete='caseade' artinya jika data dihapus maka data induk tidak ikut terhapus
    partner_id = fields.Many2one(comodel_name='res.partner',string='Partner ID',required=True, ondelete='casecade')
    pendidikan = fields.Selection(string='Pendidikan', selection=[('smp', 'SMP'), ('sma', 'SMA/SMK'), ('diploma', 'D1/D2/D3'), ('s1', 'S1'), ('s2', 'SM2'),])
    pekerjaan = fields.Char(string='Pekerjaan')
    is_menikah = fields.Boolean(string='Sudah Menikah', default=False)
    nama_pasangan = fields.Char(string='Nama Istri/Suami')
    hp_pasangan = fields.Char(string='No HP Istri/Suami')
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    no_peserta = fields.Char(string='No Peserta')

    @api.model
    def create(self, values):
        # Add code here
        values['no_peserta'] = self.env['ir.sequence'].next_by_code('seq.peserta')
        return super().create(values)
        
    
    
    
    
    
    