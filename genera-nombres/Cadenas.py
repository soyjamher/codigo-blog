#!/usr/bin/env python

import random

class Cadenas:
	consonantes = "BCDFGHJKLMNPQRSTVWXYZ"
	vocales = "AEIOU"
	repetir = "LRH"

	@classmethod
	def silaba(cls,letras = random.randint(2, 3), const = consonantes, vcls = vocales, rpt = repetir):
		if(1 == random.randint(0, 1)):
			silaba = random.choice(vcls) + random.choice(const)
			if(3==letras):
				silaba = silaba + random.choice(vcls)
		else:
			silaba = random.choice(const)
			if(3==letras and 1 == random.randint(0, 1)):
				silaba = silaba + random.choice(rpt) + random.choice(vcls)
			elif(3==letras):
				silaba = silaba + random.choice(vcls) + random.choice(const)
			else:
				silaba = silaba + random.choice(vcls)
		return silaba

	@classmethod
	def generar(cls,corto):
		cadena_generada = ""
		limite = 20
		if( 1 == corto ):
			limite = 10
		prob_espacio = random.randint(0,limite)

		if( 1 == prob_espacio or 12 == prob_espacio or 18 == prob_espacio):
			cadena_generada = cls.silaba() + " " + cls.silaba() + cls.silaba()
		elif( 6 == prob_espacio or 13 == prob_espacio or 15 == prob_espacio):
			cadena_generada = cls.silaba() + " " + cls.silaba() + cls.silaba() + cls.silaba()
		elif( 1 == corto and random.randint(1,40)%2 == 0):
			cadena_generada = cls.silaba() + cls.silaba()
		elif( ( 1 != corto and random.randint(1,40)%2 == 0) or ( 1 == corto )):
			cadena_generada = cls.silaba() + cls.silaba() + cls.silaba()
		else:
			cadena_generada = cls.silaba() + cls.silaba() + cls.silaba() + cls.silaba()
		return cadena_generada



	@classmethod
	def definirBase(cls,persona):
		a = persona.paterno.find("A")
		e = persona.paterno.find("E")
		i = persona.paterno.find("I")
		o = persona.paterno.find("O")
		u = persona.paterno.find("U")
		vocal = min([a, e, i, o, u])
		return persona.paterno[0:1] + persona.paterno[vocal] + persona.materno[0:1] + persona.nombre[0:1] + persona.yyyy[2:4] + persona.mm + persona.dd 

	@classmethod
	def crearCurp(cls,persona):
		second_ptn = persona.paterno.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace(" ","")[1:2]
		second_mtn = persona.materno.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace(" ","")[1:2]
		second_nmb = persona.nombre.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace(" ","")[1:2]
		return persona.base +  persona.sexo + persona.code_estado + second_ptn + second_mtn + second_nmb + str(random.randint(0, 9)) + str(random.randint(0, 9))

	@classmethod
	def creaRFC(cls, persona,const = consonantes, ):
		return persona.base + random.choice(const) + random.choice(const) + str(random.randint(0, 9))