# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import threading
from datetime import timedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class Move(models.Model):
    _inherit = "account.move"

    def _confirmation_sms_account_template(self, template_xmlid):
        try:
            return self.env.ref(template_xmlid)
        except ValueError:
            return False

    def _reusable_sms_call(self, template_xmlid, invoice_filters):
        """Send an SMS text reminder to custumers pay invoices"""

        template_id = self._confirmation_sms_account_template(template_xmlid)
        #_logger.info(f"################ template_id {template_id}")
        invoices = self.search(invoice_filters) or None
        #_logger.info(f"################ invoices {invoices}")
        if invoices:
            for posted_invoice in invoices:
                posted_invoice._message_sms_with_template(
                    template=template_id,
                    # template_xmlid="account_move.sms_template_data_invoice_sent",
                    # template_fallback=_("Event reminder: %s, %s.")
                    #% (posted_invoice.name, posted_invoice.partner_id.name),
                    # partner_ids=self._sms_get_default_partners().ids,
                    partner_ids=[posted_invoice.partner_id.id],
                    put_in_queue=False,
                )

    def _do_sms_reminder(self):
        ### Invoice sent: Alert by SMS Text Message
        self._reusable_sms_call(
            "account_sms.sms_template_data_invoice_sent",
            [
                ("payment_journal_id", "=", 18),  # boleto ineter
                ("state", "=", "posted"),
                ("invoice_date", "=", fields.Datetime.now().date()),
            ],
        )
        ### Invoice due date: Alert by SMS Text Message
        self._reusable_sms_call(
            "account_sms.sms_template_data_invoice_due_date",
            [
                # ("payment_journal_id", "=", 18),  # boleto ineter
                ("state", "=", "posted"),
                ("invoice_date_due", "=", fields.Datetime.now().date()),
            ],
        )
        ### Invoice overdue d+1: Alert by SMS Text Message
        self._reusable_sms_call(
            "account_sms.sms_template_data_invoice_overdue_1",
            [
                ("payment_journal_id", "=", 18),  # boleto ineter
                ("state", "=", "posted"),
                (
                    "invoice_date_due",
                    "=",
                    fields.Datetime.now().date() + timedelta(days=1),
                ),
            ],
        )
        ### Invoice overdue d+2: Alert by SMS Text Message
        self._reusable_sms_call(
            "account_sms.sms_template_data_invoice_overdue_2",
            [
                ("payment_journal_id", "=", 18),  # boleto ineter
                ("state", "=", "posted"),
                (
                    "invoice_date_due",
                    "=",
                    fields.Datetime.now().date() + timedelta(days=2),
                ),
            ],
        )
        ### Invoice overdue d+3: Alert by SMS Text Message
        self._reusable_sms_call(
            "account_sms.sms_template_data_invoice_overdue_3",
            [
                ("payment_journal_id", "=", 18),  # boleto ineter
                ("state", "=", "posted"),
                (
                    "invoice_date_due",
                    "=",
                    fields.Datetime.now().date() + timedelta(days=3),
                ),
            ],
        )
