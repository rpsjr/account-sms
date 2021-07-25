# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Account - SMS",
    "summary": "Send text messages from invoice to payment",
    "description": "Send text messages from invoice to payment",
    "category": "Hidden",
    "version": "1.0",
    "depends": ["account", "sms"],
    "data": [
        "data/sms_data.xml",
        "data/sms_invoice_cron.xml",
        # "views/res_config_settings_views.xml",
        # "wizard/confirm_stock_sms_views.xml",
        "security/ir.model.access.csv",
        "security/sms_security.xml",
    ],
    "application": False,
    "auto_install": True,
    # "post_init_hook": "_assign_default_sms_template_picking_id",
}
