
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = ['sale.order']

    line_ids = fields.One2many('sale.order.page', 'sale_id', string='Page')
    percent = fields.Integer(string='Percent', required=True)
    profit = fields.Float(string='Profit', compute='_compute_profit', store=True, readonly=True)
    total = fields.Monetary(string='Total', compute='_compute_total', store=True, readonly=True)

    @api.constrains('percent')
    def _check_percent(self):
        for rec in self:
            if rec.percent < 0 or rec.percent > 100:
                raise ValidationError(_("The percent should be between 0 and 100."))

    @api.depends('percent', 'total')
    def _compute_profit(self):
        for rec in self:
            rec.profit = (rec.percent / 100) * rec.total

    @api.depends('line_ids')
    def _compute_total(self):
        total = 0.0
        for rec in self.line_ids:
            total += rec.amount

        self.total = total


class SaleOrderPage(models.Model):
    _name = "sale.order.page"
    _description = "Sale Order Page"

    sale_id = fields.Many2one('sale.order', string='Sale')
    amount = fields.Float(string='Amount')
    date = fields.Date(string='Date')
    currency_id = fields.Many2one('res.currency', string='Currency')
