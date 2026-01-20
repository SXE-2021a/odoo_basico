# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import os


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'modelo con distintos tipos de datos'
     _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o Titulo')]


     name = fields.Char(string="Título:",size=20,required=True)
     descripcion = fields.Text(string="A Descripción:")
     alto_en_cms = fields.Integer(string="Alto en cms:")
     ancho_en_cms = fields.Integer(string="Ancho en cms:")
     longo_en_cms = fields.Integer(string="Longo en cms:")
     volume = fields.Float(string="Volume m3:",digits=(6,2),store=True,compute="_volume")
     peso = fields.Float(string="Peso en Kgs:",digits=(6,2),default=2.7)
     densidade = fields.Float(string="Densidade KG/m3:", digits=(6, 4), store=True, compute="_densidade")
     autorizado = fields.Boolean(default=False, string="¿Autorizado?:")
     sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo:")
     foto = fields.Binary(string='Foto')
     adxunto_nome = fields.Char(string="Nome Adxunto")
     adxunto = fields.Binary(string="Arquivo adxunto")
     literal = fields.Char(store=False)

     # Os campos Many2one crean un campo na BD
    # moeda_id = fields.Many2one('res.currency', domain="[('position','=','after')]", string="Moeda:")
     # Se queremos que mostre tamén o "dolar" que ten position=before lle quitamos o filtro en domain
     moeda_id = fields.Many2one('res.currency', domain="[]", string="Moeda:")
     # con domain, filtramos os valores mostrados. Pode ser mediante unha constante (vai entre comillas) ou unha variable
     # O campo currency_unit_label en versións anteriores era de tipo char, agora é de tipo json (para poder ter varias literais, en función do idioma),
     # por iso quitamos store= true
     #moeda_en_texto = fields.Char(related="moeda_id.currency_unit_label",string="Moeda en formato texto",store=True)
     moeda_en_texto = fields.Char(related="moeda_id.currency_unit_label",string="Moeda en formato texto")
     creador_da_moeda = fields.Char(related="moeda_id.create_uid.login",string="Usuario creador da moeda", store=True)
     moeda_euro_id = fields.Many2one('res.currency',
                                     default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],
                                                                                          limit=1))
     gasto_en_euros = fields.Monetary("Gasto en Euros", 'moeda_euro_id')
     moeda_dolar_id = fields.Many2one('res.currency',
                                     default=lambda self: self.env['res.currency'].search([('name', '=', "USD")],
                                                                                          limit=1))
     gasto_en_dolares = fields.Monetary("Gasto en Dolares", 'moeda_dolar_id')


     @api.depends ('alto_en_cms','ancho_en_cms','longo_en_cms')
     def _volume(self):
         for rexistro in self:
             rexistro.volume = (float(rexistro.alto_en_cms) * float(rexistro.ancho_en_cms) * float(rexistro.longo_en_cms)) /1000000

     @api.depends('peso', 'volume')
     def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)
            else:
                rexistro.densidade = 0

     @api.onchange('alto_en_cms')
     def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O campo alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
            else:
                rexistro.literal = ""


     @api.constrains('')  # Ao usar ValidationError temos que importar a libreria ValidationError
     def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)

     def _cambia_campo_sexo(self, rexistro):
         rexistro.sexo_traducido = "Hombre"

     def envio_email(self):
         meu_usuario = self.env.user
         # mail_de     Odoo pon o email que configuramos en gmail para facer o envio
         mail_reply_to = meu_usuario.partner_id.email  # o enderezo email que ten asociado o noso usuario
         mail_para = 'emaildedestino@servidordedestino.com'  # o enderezo email de destino
         mail_valores = {
             'subject': 'Aquí iría o asunto do email ',
             'author_id': meu_usuario.id,
             'email_from': mail_reply_to,
             'email_to': mail_para,
             'message_type': 'email',
             'body_html': 'Aquí iría o corpo do email cos datos por exemplo de "%s" ' % self.descripcion,
         }
         mail_id = self.env['mail.mail'].create(mail_valores)
         mail_id.sudo().send()
         return True

     def ver_contexto(self):  # Este metodo é chamado dende un botón de informacion.xml
         for rexistro in self:
             # Ao usar warning temos que importar a libreria mediante from odoo.exceptions import Warning
             # Importamos tamén a libreria os mediante import os
             # raise Warning('Contexto: %s Ruta: %s Contido do directorio %s' % (rexistro.env.context, os.getcwd(), os.listdir(os.getcwd())))

             # Warning is deprecated por iso usamos ValidationError

             raise ValidationError('Contexto: %s Ruta: %s Contido do directorio %s' % (
                 rexistro.env.context, os.getcwd(), os.listdir(os.getcwd())))
             # env.context é un diccionario  https://www.w3schools.com/python/python_dictionaries.asp
         return True