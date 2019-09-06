from odoo import models, fields, api


class SumTwoFields(models.Model):
    _name = 'sum.two.fields'
    _rec_name = 'summation'
    _description = 'SumTwoFields'

    salary = fields.Integer(string="salary")
    reward = fields.Integer(string="Reward")
    summation = fields.Integer(string="Summation", )

    @api.onchange('salary', 'reward')
    def onchange_field(self):
        if self.salary or self.reward:
            self.summation = self.salary + self.reward
