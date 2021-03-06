# -*- coding: utf-8 -*-
# © 2013-2015 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# © 2014 Serv. Tecnol. Avanzados - Pedro M. Baeza
# © 2016 Antiun Ingenieria S.L. - Antonio Espinosa
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp import models, fields, api


class PaymentMode(models.Model):
    _inherit = 'payment.mode'

    convert_to_ascii = fields.Boolean(
        string='Convert to ASCII', default=True,
        help="If active, Odoo will convert each accented caracter to "
        "the corresponding unaccented caracter, so that only ASCII "
        "caracters are used in the generated PAIN file.")
    initiating_party_issuer = fields.Char(
        string='Initiating Party Issuer', size=35,
        help="This will be used as the 'Initiating Party Issuer' in the "
        "PAIN files generated by Odoo. If not defined, Initiating Party "
        "Issuer from company will be used.\n"
        "Common format (13): \n"
        "- Country code (2, optional)\n"
        "- Company idenfier (N, VAT)\n"
        "- Service suffix (N, issued by bank)")
    initiating_party_identifier = fields.Char(
        string='Initiating Party Identifier', size=35,
        help="This will be used as the 'Initiating Party Identifier' in "
        "the PAIN files generated by Odoo. If not defined, Initiating Party "
        "Identifier from company will be used.\n"
        "Common format (13): \n"
        "- Country code (2, optional)\n"
        "- Company idenfier (N, VAT)\n"
        "- Service suffix (N, issued by bank)")
    sepa_type = fields.Char(compute="_compute_sepa_type")

    def _sepa_type_get(self):
        """Defined to be inherited by child addons, for instance:
            - account_banking_sepa_credit_transfer
            - account_banking_sepa_direct_debit
        """
        return False

    @api.multi
    @api.depends('type')
    def _compute_sepa_type(self):
        for mode in self:
            mode.sepa_type = mode._sepa_type_get()
