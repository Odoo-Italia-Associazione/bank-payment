[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/bank-payment/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/bank-payment?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
================================================================
   :alt: License AGPL-3

Batch reconciliation for transfer lines created in payment orders
=================================================================

This module allows to process with the connector technology the heavy task of
reconciliation of the receivable/payable journal entries of a payment order
against the created entries in transfer accounts.

This approach provides many advantages, similar to the ones we get
using that connector for e-commerce:

- Asynchronous: the operation is done in background, and users can
  continue to work.
- Dedicated workers: the queued jobs are performed by specific workers
  (processes). This is good for a long task, since the main workers are
  busy handling HTTP requests and can be killed if operations take
  too long, for example.
- Multiple transactions: this is an operation that doesn't need to be
  atomic, and if a line out of 100,000 fails, it is possible to catch
  it, see the error message, and fix the situation. Meanwhile, all
  other jobs can proceed.

Inspired on *account_move_batch_validate* module from Camptocamp and ACSONE.

Installation
------------

















This module requires the *connector* module, hosted on
`OCA/connector <https://github.com/OCA/connector>`_

Configuration
-------------

















This will only work for payment modes that have a transfer account set.

Usage
-----




















=====

When exporting the payment order, click on *Validate* to generate the transfer
move. One connector job will be created for each payment line for a deferred
conciliation of this line.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/173/8.0

Known issues / Roadmap
----------------------
















Bug Tracker
-----------

















Bugs are tracked on `GitHub Issues
<https://github.com/OCA/bank-payment/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
-------


































### Contributors

















* Pedro M. Baeza <pedro.baeza@tecnativa.com>

### Funders
### Maintainer

































.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

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

