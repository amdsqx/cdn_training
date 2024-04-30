from odoo import models, fields, api


# omod shortcut untuk class model
# class model untuk provinsi
class RefProvinsi(models.Model):
    _name = 'ref.provinsi'
    _description = 'Ref Provinsi'

    # ofc shortcut untuk class field char
    name = fields.Char(string='Nama Provinsi')
    kode = fields.Char(string='Kode Prvonsi')
    singkatan = fields.Char(string='Singkatan')
    keterangan = fields.Datetime(string='Keterangan')

    # untuk membagikan data ke ref.kota, jika ada class model one2many pasti ada class model lain untuk mengambil data dengan many2one, berikut berelasi dengan ref.kota untuk membagikan data provinsi yang berisi banyak data kota dalam satu provinsi
    kota_ids = fields.One2many(comodel_name='ref.kota', inverse_name='provinsi_id', string='Nama Kota')
    


# omod shortcut untuk class model
# class model untuk kota
class RefKota(models.Model):
    _name = 'ref.kota'
    _description = 'Ref Kota'

    # ofc shortcut untuk class field char
    name = fields.Char(string='Nama Kota')
    kode = fields.Char(string='Kode Kota')
    singkatan = fields.Char(string='Singkatan')
    keterangan = fields.Char(string='Keterangan')

    # untuk mengambil data kota dari provinsi, provinsi_id many2one karena mengambil data provinsi dan dalam provinsi ada data kota, comodel_name'ref.kota' adalah nama data yang untuk diambil. berikut berelasi dengan ref.kota umtuk mengambil nama kota yang ref.provinsi lempar
    provinsi_id = fields.Many2one(comodel_name='ref.provinsi', string='Nama Provinsi')
    # untuk membagikan data ke ref.kecamatan, jika ada class model one2many pasti ada class model lain untuk mengambil data dengan many2one, berikut berelasi dengan ref.kecamatan untuk membagikan data kota yang berisi banyak data kecamatan dalam satu kota
    kecamatan_ids = fields.One2many(comodel_name='ref.kecamatan', inverse_name='kota_id', string='Daftar Kecamatan')
    


# omod shortcut untuk class model
# class model untuk kecamatan
class RefKecamatan(models.Model):
    _name = 'ref.kecamatan'
    _description = 'Ref Kecamatan'

    # ofc shortcut untuk class field char
    name = fields.Char(string='Nama Kecamatan')
    kode = fields.Char(string='Kode Kecamatan')
    singkatan = fields.Char(string='Singkatan')
    keterangan = fields.Char(string='Keterangan')

    # untuk mengambil data kota dari provinsi, provinsi_id many2one karena mengambil data kecamatan dan dalam kota ada data kecamatan, comodel_name'ref.kecamatan' adalah nama data yang untuk diambil. berikut berelasi dengan ref.kota umtuk mengambil nama kecamatan yang ref.kecamatan lempar
    kota_id = fields.Many2one(comodel_name='ref.kota', string='Daftar Kota')
    # untuk membagikan data ke ref.desa, jika ada class model one2many pasti ada class model lain untuk mengambil data dengan many2one, berikut berelasi dengan ref.desa untuk membagikan data desa yang berisi banyak data desa dalam satu kecamatan
    desa_ids = fields.One2many(comodel_name='ref.desa', inverse_name='kecamatan_id', string='Daftar Desa')


# omod shortcut untuk class model
# class model untuk desa
class RefDesa(models.Model):
    _name = 'ref.desa'
    _description = 'Ref Desa'

    # ofc shortcut untuk class field char
    name = fields.Char(string='Nama Desa')
    kode = fields.Char(string='Kode Desa')
    singkatan = fields.Char(string='Singkatan')
    keterangan = fields.Char(string='Keterangan')

    # untuk mengambil data dari ref.kota
    kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Nama Kecamatan')


    

    
    
    
    

    
    
    
    
