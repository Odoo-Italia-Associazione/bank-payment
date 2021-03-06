[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/bank-payment/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/bank-payment?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Banking addons for Odoo
=======================

This project focuses on in- and export of banking communication.

Other features can now be found in these repositories:
 * https://github.com/OCA/bank-statement-import
 * https://github.com/OCA/bank-statement-reconcile

[//]: # (addons)


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_banking_mandate](account_banking_mandate/) | 8.0.0.2.1 | 8.0.0.2.0 | Banking mandates
[account_banking_pain_base](account_banking_pain_base/) | 8.0.0.4.1 | 8.0.0.4.0 | Base module for PAIN file generation
[account_banking_payment_export](account_banking_payment_export/) | 8.0.0.3.0 | :repeat: | Account Banking - Payments Export Infrastructure
[account_banking_payment_transfer](account_banking_payment_transfer/) | 8.0.0.3.1 | :repeat: | Account Banking - Payments Transfer Account
[account_banking_sepa_credit_transfer](account_banking_sepa_credit_transfer/) | 8.0.0.5.2 | 8.0.0.5.0 | Create SEPA XML files for Credit Transfers
[account_banking_sepa_direct_debit](account_banking_sepa_direct_debit/) | 8.0.0.5.1 | 8.0.0.5.0 | Create SEPA files for Direct Debit
[account_banking_tests](account_banking_tests/) | 8.0.0.1.0 | :repeat: | Banking Addons - Tests
[account_direct_debit](account_direct_debit/) | 8.0.2.1.0 | :repeat: | Direct Debit
[account_import_line_multicurrency_extension](account_import_line_multicurrency_extension/) | 8.0.1.1.0 | :repeat: | Add an improved view for move line import in bank statement
[account_payment_blocking](account_payment_blocking/) | 8.0.1.0.0 | :repeat: | Prevent invoices under litigation to be proposed in payment orders.
[account_payment_include_draft_move](account_payment_include_draft_move/) | 8.0.1.0.0 | :repeat: | Account Payment Draft Move
[account_payment_mode_term](account_payment_mode_term/) | 8.0.0.1.2 | :repeat: | Account Banking - Payments Term Filter
[account_payment_partner](account_payment_partner/) | 8.0.0.2.0 | :repeat: | Adds payment mode on partners and invoices
[account_payment_purchase](account_payment_purchase/) | 8.0.1.0.0 | :repeat: | Adds Bank Account and Payment Mode on Purchase Orders
[account_payment_sale](account_payment_sale/) | 8.0.1.0.0 | :repeat: | Adds payment mode on sale orders
[account_payment_sale_stock](account_payment_sale_stock/) | 8.0.1.0.0 | :repeat: | Manage payment mode when invoicing a sale from picking
[account_payment_transfer_reconcile_batch](account_payment_transfer_reconcile_batch/) | 8.0.1.0.0 | :repeat: | Batch Reconciliation for transfer moves
[account_voucher_killer](account_voucher_killer/) | 8.0.1.0.0 | :repeat: | Accounting voucher killer
[portal_payment_mode](portal_payment_mode/) | 8.0.1.0.0 | :repeat: | Adds payment mode ACL's for portal users


Unported addons
---------------
addon | version | OCA version | summary
--- | --- | --- | ---
[bank_statement_instant_voucher](bank_statement_instant_voucher/) | 1.0r028 (unported) | :repeat: | Bank statement instant voucher

[//]: # (end addons)


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Moduli aggiuntivi per Banche
============================

Progetto per la gestione dell'interfacciamento con le banche.

Differenze rispetto localizzazione ufficiale Odoo/OCA

Descrizione | Odoo Italia | OCA
--- | --- | ---
Coverage |  [![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0) | [![codecov](https://codecov.io/gh/OCA/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/OCA/bank-payment/branch/8.0)
Test compatibilità OCA e Odoo | :white_check_mark: | :white_check_mark:
Bonifici Italia | Si, standard CBI | No
SDD Italia | Si, standard CBI | No
account_banking_pain_base | Modifiche per CBI (Italia) | Solo EU
account_banking_mandate | Validazione riassegna numero, se assente | Validazione ripristina numero anche se assente

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017, Odoo Italia Associazione replaces OCA members of Italy are developping code under Odoo Proprietary License.
Odoo Italia Associazione distributes only code under AGPL free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 sostituisce gli sviluppatori italiani di OCA che sviluppano
con Odoo Proprietary License a pagamento.

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](http://www.gnu.org/licenses/agpl-3.0.html)

[//]: # (end copyright)


