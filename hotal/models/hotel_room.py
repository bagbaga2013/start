from odoo import models, fields,api

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'
    _rec_name ='room_type'
    name = fields.Char(string='رقم الغرفة', required=True)
    hotel_id = fields.Many2one('my.hotel', string='الفندق' )
    t1 = fields.Char(related='hotel_id.code')

    #t2 =fields.char(related ='hotel_id.city')
    room_type = fields.Selection([
        ('single', 'مفردة'),
        ('double', 'مزدوجة'),
        ('suite', 'جناح'),
    ], string='نوع الغرفة', required=True)

    idmyroom = fields.One2many(
        'hotel.reservation',   # اسم الموديل (technical)
        'room_id',             # اسم Many2one في الموديل الآخر
        string='الحجوزات'
    )
  
    #ittag = fields.Many2many('my.tag')
    price = fields.Float(string='سعر الليلة',digits=(0,5))
    capacity = fields.Integer(string='عدد الأشخاص')
    is_available = fields.Boolean(string='متاحة', default=True)
    active = fields.Boolean(default=True)

    @api.constrains('price')
    def _check_price(self):
         for record in self:
            if record.price <= 0:
                raise ValidationError('❌ السعر يجب أن يكون أكبر من صفر')
          