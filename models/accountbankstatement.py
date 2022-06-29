
from odoo import models, fields, api

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"
    _description = "Bank Statement"

    @api.depends('line_ids', 'balance_start', 'line_ids.amount', 'balance_end_real')
    def _end_balance(self):
        for statement in self:
            statement.total_entry_encoding = sum([line.amount for line in statement.line_ids])
            statement.balance_end = statement.balance_start + statement.total_entry_encoding
            statement.difference = statement.balance_end_real - statement.balance_end
            statement.balance_end_real = statement.balance_end

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement.line"
    _description = "Bank Statement"




