[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/bank-payment/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/bank-payment?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

    :alt: License: AGPL-3
=========================

Account Banking - Payments Transfer Account
===========================================

Payment order reconciliation infrastructure

This module reconciles invoices as soon as the payment order
is sent, by creating a move to a transfer account (aka suspense account).
When the moves on the suspense account are reconciled (typically through
the bank statement reconciliation, the payment order moves to the done
status).
    
Installation
------------

















This module depends on :
* account_banking_payment_export

This module is part of the OCA/bank-payment suite.

Configuration
-------------

















To configure this module, you need to:

 * create a transfer account who allow reconciliation : option "Allow Reconciliation" activated.
 * configure transfer account on payment mode. Go to the menu Accounting > Configuration > Miscellaneous > Payment Mode and complete the section "Transfer move settings".

Usage
-----




















=====

This module allows to reconcile transfer account and invoice by selecting on a payment order a payment mode with the option "transfer account" activated.


For further information, please visit:

 * https://www.odoo.com/forum/help-1

Known issues / Roadmap
----------------------

















 * No known issues
 
Bug Tracker
-----------

















Bugs are tracked on `GitHub Issues <https://github.com/OCA/bank-payment/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/bank-payment/issues/new?body=module:%20account_banking_payment_transfer%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
-------


































### Contributors

















* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Adrien Peiffer <adrien.peiffer@acsone.eu>
* Alexis de Lattre
* Matt Choplin
* Alexandre Fayolle
* Danimar Ribeiro
* Jose Maria Alzaga <jose.alzaga@aselcis.com>

### Funders
### Maintainer

































.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

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

[//]: # (addons)

[//]: # (end addons)

