from odoo import models, fields, api, _


class TaskOne(models.Model):
    _name = 'task.one'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Task One'

    name = fields.Char(string="Name")
    user_ids = fields.Many2many('res.users', 'users_task', 'users', 'task', string="Users")
    user_line_ids = fields.One2many('user.line', 'task_id', string='User line')

    def action_test(self):
        if self.user_ids:
            vals = {
                'users_ids': self.user_ids,
                'task_id': self.id
            }
            self.user_line_ids.create(vals)
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': _('You should enter the value in user field'),
                    'sticky': False,  # for automatically disappear
                    'type': 'danger',  # for color
                }
            }


class UserLine(models.Model):
    _name = 'user.line'
    _description = 'User Line'

    task_id = fields.Many2one('task.one', string='Task')
    users_ids = fields.Many2many('res.users', 'users_line_task', 'users', 'line_tags', string='Users')
