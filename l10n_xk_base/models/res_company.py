# -*- coding: utf-8 -*-
# Copyright 2017 bole ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.tools.translate import _


class Company(models.Model):
    _inherit = "res.company"

    @api.depends('country_id')
    def _check_origin_country_xk(self):
        for company in self:
            company.kosovo = company.country_id and company.country_id.code == 'XK'

    kosovo = fields.Boolean(
        string="Kosovo",
        compute="_check_origin_country_xk",
        # technical field for show/hide kosovo settings, never to be exposed to UI, alwasy invisible!
    )

    l10n_xk_biznesit = fields.Char(
        string=_("Nr.Biznesit"),
        required=False,
        translate=False,
        readonly=True
    )
    l10n_xk_fiskal = fields.Char(
        string=_("Nr.Fiskal"),
        required=False,
        translate=False,
        readonly=True
    )
