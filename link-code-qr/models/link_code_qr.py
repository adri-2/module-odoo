# -*- coding: utf-8 -*-
import base64
import io
import qrcode
from odoo import models, fields, api

class LinkCodeQr(models.Model):
    _name = 'link_code_qr'  # Nom correct du modèle
    _description = 'QR Code for Product'

    # Relation vers product.product
    product_id = fields.Many2one('product.product', string="Product", required=True)

    # Champ pour l'URL du produit
    product_url = fields.Char(string="Product URL", compute='_compute_product_url', store=True)

    # Champ pour l'image QR Code du produit
    image_qr = fields.Image("Code QR du produit", max_width=200, max_height=200)

    @api.depends('product_id')
    def _compute_product_url(self):
        for record in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')  # URL de base du site
            if record.product_id:
                # Génération de l'URL du produit
                name_product_site = record.product_id.name
                name_product_site=name_product_site.replace(' ','-')
                record.product_url = f"{base_url}/shop/{name_product_site}"

                # Génération du QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(record.product_url)
                qr.make(fit=True)

                # Convertir en image
                img = qr.make_image(fill='black', back_color='white')

                # Sauvegarder l'image dans un buffer
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                qr_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

                # Assigner l'image encodée en base64 au champ image_qr
                record.image_qr = qr_image_base64

