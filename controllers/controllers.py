# -*- coding: utf-8 -*-
# from odoo import http


# class AccountingBankStatementEndBalance(http.Controller):
#     @http.route('/accounting_bank_statement_end_balance/accounting_bank_statement_end_balance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accounting_bank_statement_end_balance/accounting_bank_statement_end_balance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('accounting_bank_statement_end_balance.listing', {
#             'root': '/accounting_bank_statement_end_balance/accounting_bank_statement_end_balance',
#             'objects': http.request.env['accounting_bank_statement_end_balance.accounting_bank_statement_end_balance'].search([]),
#         })

#     @http.route('/accounting_bank_statement_end_balance/accounting_bank_statement_end_balance/objects/<model("accounting_bank_statement_end_balance.accounting_bank_statement_end_balance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accounting_bank_statement_end_balance.object', {
#             'object': obj
#         })
