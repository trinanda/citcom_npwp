# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    npwp = fields.Char(string='NPWP')
    total_sales = fields.Float(string='Total Sales', compute='_get_total_sales')

    def _get_total_sales(self):
        for rec in self:
            sales = self.env['sale.order'].search([('partner_id', '=', rec.id)])
            for so in sales:
                rec.total_sales += so.amount_total
