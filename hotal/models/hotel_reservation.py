from odoo import models, fields

class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'

    name = fields.Char(string='رقم الحجز', required=True)
    customer_id = fields.Many2one('res.partner', string='العميل', required=True)
    room_id = fields.Many2one('hotel.room', string='الغرفة')

    check_in = fields.Date(string='تاريخ الدخول', required=True)
    check_out = fields.Date(string='تاريخ الخروج', required=True)

    state = fields.Selection([
        ('draft', 'مسودة'),
        ('confirm', 'مؤكد'),
        ('done', 'منتهي'),
        ('cancel', 'ملغي'),
    ], default='draft', string='الحالة')

    total_price = fields.Float(string='المبلغ الإجمالي', compute='_compute_total')

    def _compute_total(self):
        for rec in self:
            if rec.check_in and rec.check_out:
                days = (rec.check_out - rec.check_in).days
                rec.total_price = days * rec.room_id.price
            else:
                rec.total_price = 0
