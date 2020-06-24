from odoo import models


class Themegrancorte(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_grancorte_post_copy(self, mod):
        # Change color preset
        self.enable_view('theme_common.option_colors_05_variables')
