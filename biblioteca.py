from odoo import models, fields, api

class Socio(models.Model):
    _name = 'socio'
    num_socio = fields.Integer("Numero socio", required=True)
    nombre = fields.Char("Nombre socio")
    apellidos = fields.Char("Apellidos socio")
    socio_preferente = fields.Boolean("Preferente?")
    direccion = fields.Char("Direccion")
    codpostal = fields.Integer("Codigo postal", size = 5)
    poblacion = fields.Char("Poblacion")

class Autor(models.Model):
    _name = 'autor'
    dni = fields.Char("Dni autor", required=True)
    nombre = fields.Char("Nombre autor")
    apellidos = fields.Char("Apellidos autor")
    direccion = fields.Char("Direccion autor")

class Libros(models.Model):
    _name='libros'
    codigo=fields.Integer('Codigo de libro')
    titulo=fields.Char('Titulo de libro')
    autor=fields.Char('Autor del libro')
    editorial=fields.Char('Editorial del libro')
    fechacompra=fields.Date('Fecha de compra') #?
    preciocompra=fields.Float('Precio de compra')
    categoria=fields.Selection([('intriga','intriga'),('drama','drama'),('infantil','infantil'),('aventuras','aventuras'),('historia','historia')],'Categoria')
    dniautor=fields.Many2many('autor','Dniautor') #IMPORTANTE
    antiguedad=fields.Integer('Antiguedad',compute='calcular_antiguedad')

    @api.depends('fechacompra')
    def calcular_antiguedad(self):
        self.antiguedad=fields.Date.today().year-self.fechacompra.year
class Prestamos(models.Model):
    _name='prestamos'
    codigo=fields.Integer('Codigo prestamo')
    fecha=fields.Datetime('Fecha y Hora del prestamo') 
    numsocio=fields.One2many('socio','numsocio','Prestamo a socio')
    codigolibro=fields.One2many('libros','codigo','Codigo libro prestamo')
    diasprestado=fields.Integer('Dias prestado',compute='calcular_prestamo')

    @api.depends('fecha')
    def calcular_prestamo(self):
        self.diasprestado=fields.Date().today()-self.fecha