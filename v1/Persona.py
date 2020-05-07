#!/usr/bin/env python

from datetime import date 
from Cadenas import Cadenas

import random

class Persona:
    var_sexo = "HM"
    arr_estados = [["AGUASCALIENTES", "AS"],["BAJA CALIFORNIA", "BC"],["BAJA CALIFORNIA SUR", "BS"],["CAMPECHE", "CC"],["COAHUILA", "CL"],["COLIMA", "CM"],["CHIAPAS", "CS"],["CHIHUAHUA", "CH"],["DISTRITO FEDERAL", "DF"],["DURANGO", "DG"],["GUANAJUATO", "GT"],["GUERRERO", "GR"],["HIDALGO", "HG"],["JALISCO", "JC"],["MÉXICO", "MC"],["MICHOACÁN", "MN"],["MORELOS", "MS"],["NAYARIT", "NT"],["NUEVO LEÓN", "NL"],["OAXACA", "OC"],["PUEBLA", "PL"],["QUERÉTARO", "QT"],["QUINTANA ROO", "QR"],["SAN LUIS POTOSÍ", "SP"],["SINALOA", "SL"],["SONORA", "SR"],["TABASCO", "TC"],["TAMAULIPAS", "TS"],["TLAXCALA", "TL"],["VERACRUZ", "VZ"],["YUCATÁN", "YN"],["ZACATECAS", "ZS"],["NACIDO EN EL EXTRANJERO", "NE"]]
    
    def __init__(self, sexo = var_sexo,estados = arr_estados):
        self.sexo = random.choice(sexo)
        intEstado = random.randint(1, 32)
        self.estado = estados[intEstado][0]
        self.code_estado = estados[intEstado][1]
        self.nombre = Cadenas.generar(1)
        self.paterno = Cadenas.generar(0)
        self.materno = Cadenas.generar(0)
        self.yyyy = str(random.randint(1965,date.today().year - 18))
        mm = str(random.randint(1, 12))
        if( len(mm) < 2 ):
            mm = "0" + mm
        self.mm = mm
        dd = str(random.randint(1, 28))
        if( len(dd) < 2 ):
            dd = "0" + dd
        self.dd = dd
        self.base = Cadenas.definirBase(self)
        self.curp = Cadenas.crearCurp(self)
        self.rfc = Cadenas.creaRFC(self)