# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zhigailov(models.Model):
	_name = 'zhigailov.zhigailov'

	name = fields.Char(string='ФИО', required=True)
	photo = fields.Binary(string='Image')
	post = fields.Selection([('president', 'Президент'), ('prime_minister', 'Премьер министр'),('LDPR party chairman', 'председатель партии ЛДПР'), ('others', 'Others')], string='Должность')
	job_date = fields.Date(string="Дата устроиства")
	chief = fields.Char(string='Начальник', required=True)