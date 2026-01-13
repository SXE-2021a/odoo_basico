# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pedido(models.Model):
     _name = 'odoo_basico.pedido'
     _description = 'modelo para pedido'

     name = fields.Char(required=True, size=20, string="Identificador de Pedido")
     # Os campos One2many Non se almacenan na BD
     lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')