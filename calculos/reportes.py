from random import choice
from decimal import Decimal


def generadorCadenaConsulta():
    cadena = ''
    charts = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    contador = 0

    while contador < 10:
        cadena += choice(charts)
        contador +=1
    
    return cadena

    

def gen():
    cadena = []
    charts = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    for k in range(1, 10+1):
        cadena.append(choice(charts))

    cadena = ''.join(cadena)
    return cadena



def extraccionValor(Modelo, id_modelo):
    # Extrae el valor del campo nombre de un modelo indicandole el pk del registro
    if id_modelo is None:
        return None
    else:
        registro = Modelo.objects.get(pk=id_modelo)
        elemento = registro.nombre
        return elemento


### Dererminar Valor para grafica de elementos
def valor_str(v):
    if v == None:
        return "N.D."
    else:
        return str(v)

def valor_str_SD(v):
    if v == None:
        return "S.D."
    else:
        return str(v)




##DETERMINAR LA CLASIFICACION DE LOS ELEMENTOS ENTRE:
#   Muy Bajo
#   Bajo
#   Moderadamente Bajo
#   Mediano
#   Moderadamente Alto
#   Alto
#   Muy Alto

def clas_N(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <=3:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 3 and v <= 5:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 5 and v <= 10:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 10 and v <= 20:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 20 and v <= 50:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 50 and v <= 100:
            clas = 'Alto'
            val = 54 * 6
        elif v > 100:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
        
    else:
        return {'clasificacion': "N.D", 'valor':0}
       


def clas_P(v, tipo):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if tipo == 'P-Bray':
            if v <=4:
                clas = 'Muy Bajo'
                val = 54 * 1
            elif v > 4 and v <= 10:
                clas = 'Bajo'
                val = 54 * 2
            elif v > 10 and v <= 20:
                clas = 'Moderadamente Bajo'
                val = 54 * 3
            elif v > 20 and v <= 30:
                clas = 'Mediano'
                val = 54 * 4
            elif v > 30 and v <= 40:
                clas = 'Moderadamente Alto'
                val = 54 * 5
            elif v > 40 and v <= 60:
                clas = 'Alto'
                val = 54 * 6
            elif v > 60:
                clas = 'Muy Alto'
                val = 54 * 7
            return {'clasificacion': clas, 'valor':val}
        
        elif tipo == 'P-Olsen':
            if v <=4:
                clas = 'Muy Bajo'
                val = 54 * 1
            elif v > 4 and v <= 9:
                clas = 'Bajo'
                val = 54 * 2
            elif v > 9 and v <= 15:
                clas = 'Moderadamente Bajo'
                val = 54 * 3
            elif v > 15 and v <= 20:
                clas = 'Mediano'
                val = 54 * 4
            elif v > 20 and v <= 25:
                clas = 'Moderadamente Alto'
                val = 54 * 5
            elif v > 25 and v <= 35:
                clas = 'Alto'
                val = 54 * 6
            elif v > 35:
                clas = 'Muy Alto'
                val = 54 * 7
            return {'clasificacion': clas, 'valor':val}
        
    else:
        return {'clasificacion': "N.D", 'valor':0}



def clas_K(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <=100:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 100 and v <= 150:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 150 and v <= 200:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 200 and v <= 300:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 300 and v <= 600:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 600 and v <= 1000:
            clas = 'Alto'
            val = 54 * 6
        elif v > 1000:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}

    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Ca(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <=500:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 500 and v <= 750:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 750 and v <= 1500:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 1500 and v <= 2500:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 2500 and v <= 4000:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 4000 and v <= 6000:
            clas = 'Alto'
            val = 54 * 6
        elif v > 6000:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
       return {'clasificacion': "N.D", 'valor':0}


def clas_Mg(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <=50:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 50 and v <= 100:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 100 and v <= 200:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 200 and v <= 400:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 400 and v <= 800:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 800 and v <= 1200:
            clas = 'Alto'
            val = 54 * 6
        elif v > 1200:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Na(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v < 20:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v >= 20 and v < 30:
            clas = 'Bajo'
            val = 54 * 2
        elif v >= 30 and v < 50:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v >= 50 and v < 100:
            clas = 'Mediano'
            val = 54 * 4
        elif v >= 100 and v <= 160:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 160 and v <= 170:
            clas = 'Alto'
            val = 54 * 6
        elif v > 170:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Fe(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 3:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 3 and v <= 5:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 5 and v <= 8:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 8 and v <= 12:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 12 and v <= 25:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 25 and v <= 49:
            clas = 'Alto'
            val = 54 * 6
        elif v > 49:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Zn(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v < 0.31:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v >= 0.31 and v <= 0.6:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 0.6 and v <= 1.2:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 1.2 and v < 2.51:
            clas = 'Mediano'
            val = 54 * 4
        elif v >= 2.51 and v <= 5:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 5 and v <= 8:
            clas = 'Alto'
            val = 54 * 6
        elif v > 8:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Mn(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 2:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 2 and v <= 4:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 4 and v <= 7:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 7 and v <= 12:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 12 and v <= 25:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 25 and v <= 50:
            clas = 'Alto'
            val = 54 * 6
        elif v > 50:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Cu(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v < 0.21:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v >= 0.21 and v < 0.51:
            clas = 'Bajo'
            val = 54 * 2
        elif v >= 0.51 and v < 0.81:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v >= 0.81 and v < 1.21:
            clas = 'Mediano'
            val = 54 * 4
        elif v >= 1.21 and v < 1.81:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v >= 1.81 and v < 2.51:
            clas = 'Alto'
            val = 54 * 6
        elif v >= 2.51:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}



def clas_B(v):
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 0.4:
            clas = 'Muy Bajo'
            val = 54 * 1
        elif v > 0.4 and v <= 0.7:
            clas = 'Bajo'
            val = 54 * 2
        elif v > 0.7 and v <= 1.1:
            clas = 'Moderadamente Bajo'
            val = 54 * 3
        elif v > 1.1 and v <= 1.5:
            clas = 'Mediano'
            val = 54 * 4
        elif v > 1.5 and v <= 2:
            clas = 'Moderadamente Alto'
            val = 54 * 5
        elif v > 2 and v <= 3:
            clas = 'Alto'
            val = 54 * 6
        elif v > 3:
            clas = 'Muy Alto'
            val = 54 * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


# RELACIÓN DE BASES DE CAMBIO
## Obtención del valor de la escala para graficar
## Clasificaión:
"""
Muy Alto
Alto
Mediano
Bajo
Muy Bajo
Escala Base = 30
"""
def clas_Ca_Mg(v):
    base = 30
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 1:
            clas = 'Muy Bajo'
            val = base * 1
        elif v > 1 and v <= 2:
            clas = 'Bajo'
            val = base * 2
        elif v > 2 and v <= 6:
            clas = 'Mediano'
            val = base * 3
        elif v > 6 and v <= 8:
            clas = 'Alto'
            val = base * 4
        elif v > 8:
            clas = 'Muy Alto'
            val = base * 5
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Mg_K(v):
    base = 30
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 1:
            clas = 'Muy Bajo'
            val = base * 1
        elif v > 1 and v <= 2:
            clas = 'Bajo'
            val = base * 2
        elif v > 2 and v <= 3:
            clas = 'Mediano'
            val = base * 3
        elif v > 3 and v <= 4:
            clas = 'Alto'
            val = base * 4
        elif v > 4:
            clas = 'Muy Alto'
            val = base * 5
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_CaMg_K(v):
    base = 30
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 10:
            clas = 'Muy Bajo'
            val = base * 1
        elif v > 10 and v <= 20:
            clas = 'Bajo'
            val = base * 2
        elif v > 20 and v <= 30:
            clas = 'Mediano'
            val = base * 3
        elif v > 30 and v <= 40:
            clas = 'Alto'
            val = base * 4
        elif v > 40:
            clas = 'Muy Alto'
            val = base * 5
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_Ca_K(v):
    base = 30
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 5:
            clas = 'Muy Bajo'
            val = base * 1
        elif v > 5 and v <= 10:
            clas = 'Bajo'
            val = base * 2
        elif v > 10 and v <= 15:
            clas = 'Mediano'
            val = base * 3
        elif v > 15 and v <= 20:
            clas = 'Alto'
            val = base * 4
        elif v > 20:
            clas = 'Muy Alto'
            val = base * 5
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}




# EXTRACTO DE SALINIDAD Y SODICIDAD
## Obtención del valor de la escala para graficar
## Clasificaión:
"""
Muy Alto
Alto
Mod. Alto
Mediano
Mod. Bajo
Bajo
Muy Bajo
Escala Base = 30
"""
def clas_Sales(v):
    base = 30
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v <= 1:
            clas = 'Muy Bajo'
            val = base * 1
        elif v > 1 and v <= 2:
            clas = 'Bajo'
            val = base * 2
        elif v > 2 and v <= 3:
            clas = 'Mod. Bajo'
            val = base * 3
        elif v > 3 and v <= 5:
            clas = 'Mediano'
            val = base * 4
        elif v > 5 and v <= 7:
            clas = 'Mod. Alto'
            val = base * 5
        elif v > 7 and v <= 10:
            clas = 'Alto'
            val = base * 6
        elif v > 10:
            clas = 'Muy Alto'
            val = base * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def clas_RAS(v):
    base = 30
    if (type(v) == int or type(v) == float or type(v) == Decimal) and v >= 0:
        if v == 0:
            clas = 'Muy Bajo'
            val = base * 1
        elif v > 0 and v <= 3:
            clas = 'Bajo'
            val = base * 2
        elif v > 3 and v <= 5:
            clas = 'Mod. Bajo'
            val = base * 3
        elif v > 5 and v <= 8:
            clas = 'Mediano'
            val = base * 4
        elif v > 8 and v <= 12:
            clas = 'Mod. Alto'
            val = base * 5
        elif v > 12 and v <= 25:
            clas = 'Alto'
            val = base * 6
        elif v > 25:
            clas = 'Muy Alto'
            val = base * 7
        return {'clasificacion': clas, 'valor':val}
    else:
        return {'clasificacion': "N.D", 'valor':0}


def requerimiento_base(cultivo):
    if cultivo == 'Alfalfa':
        return {
        'Humedad': 0,
        'Req_N': 27,
        'Req_P': 2.5,
        'Req_K': 21,
        'Req_Ca': 12,
        'Req_Mg': 3,
        'Req_S': 3.5,
        'Req_B': 0.03,
        'Req_Cl': 0,
        'Req_Cu': 0.007,
        'Req_Fe': 0.04,
        'Req_Mn': 0.025,
        'Req_Mo': 0.0003,
        'Req_Zn': 0.015,
        'Req_Ni': 0,
        }
    elif cultivo == 'Arroz':
        return {
        'Humedad': 13,
        'Req_N': 22.2,
        'Req_P': 4,
        'Req_K': 26.2,
        'Req_Ca': 2.8,
        'Req_Mg': 2.4,
        'Req_S': 0.94,
        'Req_B': 0.016,
        'Req_Cl': 9.7,
        'Req_Cu': 0.027,
        'Req_Fe': 0.35,
        'Req_Mn': 0.37,
        'Req_Mo': 0,
        'Req_Zn': 0.04,
        'Req_Ni': 0,
        }
    elif cultivo == 'Cacahuate':
        return {
        'Humedad': 14.5,
        'Req_N': 69,
        'Req_P': 7,
        'Req_K': 35,
        'Req_Ca': 18.7,
        'Req_Mg': 0,
        'Req_S': 4,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0
        }
    elif cultivo == 'Canola':
        return {
        'Humedad': 8,
        'Req_N': 60,
        'Req_P': 15,
        'Req_K': 65,
        'Req_Ca': 33,
        'Req_Mg': 10,
        'Req_S': 12,
        'Req_B': 0.09,
        'Req_Cl': 0,
        'Req_Cu': 0.05,
        'Req_Fe': 0.21,
        'Req_Mn': 0.43,
        'Req_Mo': 12,
        'Req_Zn': 0.15,
        'Req_Ni': 0,
        }
    elif cultivo == 'Caña de Azucar':
        return {
        'Humedad': 0,
        'Req_N': 1.43,
        'Req_P': 0.19,
        'Req_K': 1.74,
        'Req_Ca': 0.87,
        'Req_Mg': 0.49,
        'Req_S': 0.44,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Cebada':
        return {
        'Humedad': 13.5,
        'Req_N': 26.3,
        'Req_P': 4,
        'Req_K': 19,
        'Req_Ca': 19.7,
        'Req_Mg': 0,
        'Req_S': 4.15,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Cebolla':
        return {
        'Humedad': 0,
        'Req_N': 3.9,
        'Req_P': 0.6,
        'Req_K': 4,
        'Req_Ca': 4.4,
        'Req_Mg': 0.7,
        'Req_S': 0,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Chile':
        return {
        'Humedad': 0,
        'Req_N': 3.7,
        'Req_P': 0.5,
        'Req_K': 3.8,
        'Req_Ca': 1.2,
        'Req_Mg': 0.7,
        'Req_S': 0,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Girasol':
        return {
        'Humedad': 12.5,
        'Req_N': 40,
        'Req_P': 11,
        'Req_K': 29,
        'Req_Ca': 18,
        'Req_Mg': 11,
        'Req_S': 5,
        'Req_B': 0.165,
        'Req_Cl': 0,
        'Req_Cu': 0.019,
        'Req_Fe': 0.261,
        'Req_Mn': 0.055,
        'Req_Mo': 0.029,
        'Req_Zn': 0.099,
        'Req_Ni': 0,
        }
    elif cultivo == 'Jitomate':
        return {
        'Humedad': 0,
        'Req_N': 2.8,
        'Req_P': 0.4,
        'Req_K': 4.5,
        'Req_Ca': 2.8,
        'Req_Mg': 0.7,
        'Req_S': 0.9,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Lechuga':
        return {
        'Humedad': 0,
        'Req_N': 2,
        'Req_P': 0.5,
        'Req_K': 4.3,
        'Req_Ca': 0.9,
        'Req_Mg': 0.2,
        'Req_S': 0,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Maíz':
        return {
        'Humedad': 14.5,
        'Req_N': 22,
        'Req_P': 4,
        'Req_K': 19,
        'Req_Ca': 3,
        'Req_Mg': 3,
        'Req_S': 4,
        'Req_B': 0.02,
        'Req_Cl': 0.444,
        'Req_Cu': 0.013,
        'Req_Fe': 0.125,
        'Req_Mn': 0.189,
        'Req_Mo': 0.001,
        'Req_Zn': 0.053,
        'Req_Ni': 0,
        }
    elif cultivo == 'Sorgo':
        return {
        'Humedad': 14.5,
        'Req_N': 30,
        'Req_P': 4.4,
        'Req_K': 20.8,
        'Req_Ca': 4,
        'Req_Mg': 4.5,
        'Req_S': 3.75,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }
    elif cultivo == 'Soya':
        return {
        'Humedad': 13.5,
        'Req_N': 75,
        'Req_P': 7,
        'Req_K': 39,
        'Req_Ca': 16,
        'Req_Mg': 9,
        'Req_S': 4.5,
        'Req_B': 0.025,
        'Req_Cl': 0.237,
        'Req_Cu': 0.025,
        'Req_Fe': 0.3,
        'Req_Mn': 0.15,
        'Req_Mo': 0.005,
        'Req_Zn': 0.06,
        'Req_Ni': 0,
        }
    elif cultivo == 'Trigo':
        return {
        'Humedad': 13.5,
        'Req_N': 30,
        'Req_P': 5,
        'Req_K': 19,
        'Req_Ca': 3,
        'Req_Mg': 4,
        'Req_S': 5,
        'Req_B': 0.025,
        'Req_Cl': 0,
        'Req_Cu': 0.01,
        'Req_Fe': 0.137,
        'Req_Mn': 0.07,
        'Req_Mo': 0,
        'Req_Zn': 0.052,
        'Req_Ni': 0,
        }
    
    else:
        return {
        'Humedad': 0,
        'Req_N': 0,
        'Req_P': 0,
        'Req_K': 0,
        'Req_Ca': 0,
        'Req_Mg': 0,
        'Req_S': 0,
        'Req_B': 0,
        'Req_Cl': 0,
        'Req_Cu': 0,
        'Req_Fe': 0,
        'Req_Mn': 0,
        'Req_Mo': 0,
        'Req_Zn': 0,
        'Req_Ni': 0,
        }

def calculo_requ(rend_kg, humedad, req):
    val = rend_kg * Decimal(((100 - humedad) / 100) * (req / 1000))
    return val

def requerimiento_Nutrientes(cultivo, rendimiento):
    if type(cultivo) == str:
        cultivos_existentes = [
                                'Alfalfa', 'Arroz', 'Cacahuate', 'Canola', 'Caña de Azucar', 'Cebada', 'Cebolla', 
                                'Chile', 'Girasol', 'Jitomate', 'Lechuga', 'Maíz', 'Sorgo', 'Soya', 'Trigo'
                                ]
        if cultivo in cultivos_existentes:
            if (type(rendimiento) == int or type(rendimiento) == float or type(rendimiento) == Decimal) and rendimiento >= 0:
                rend_kg = rendimiento * 1000
                resultado = requerimiento_base(cultivo)

                N = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_N']), 2)
                P = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_P']), 2)
                K = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_K']), 2)
                Ca = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Ca']), 2)
                Mg = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Mg']), 2)
                S = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_S']), 2)
                B = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_B']), 2)
                Cl = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Cl']), 2)
                Cu = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Cu']), 2)
                Fe = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Fe']), 2)
                Mn = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Mn']), 2)
                Mo = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Mo']), 2)
                Zn = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Zn']), 2)
                Ni = round(calculo_requ(rend_kg, resultado['Humedad'], resultado['Req_Ni']), 2)

                return {
                'N': N,
                'P': P,
                'K': K,
                'Ca': Ca,
                'Mg': Mg,
                'S': S,
                'B': B,
                'Cl': Cl,
                'Cu': Cu,
                'Fe': Fe,
                'Mn': Mn,
                'Mo': Mo,
                'Zn': Zn,
                'Ni': Ni,
                }
            else:
                return {
                'N':'N.D.', 'P':'N.D.', 'K':'N.D.', 'Ca':'N.D.', 'Mg':'N.D.', 'S':'N.D.', 'B':'N.D.',
                'Cl':'N.D.', 'Cu':'N.D.', 'Fe':'N.D.', 'Mn':'N.D.', 'Mo':'N.D.', 'Zn':'N.D.', 'Ni':'N.D.'
                }

        else:
            return {
                'N':'N.D.', 'P':'N.D.', 'K':'N.D.', 'Ca':'N.D.', 'Mg':'N.D.', 'S':'N.D.', 'B':'N.D.',
                'Cl':'N.D.', 'Cu':'N.D.', 'Fe':'N.D.', 'Mn':'N.D.', 'Mo':'N.D.', 'Zn':'N.D.', 'Ni':'N.D.'
                }
    else:
        return {
                'N':'N.D.', 'P':'N.D.', 'K':'N.D.', 'Ca':'N.D.', 'Mg':'N.D.', 'S':'N.D.', 'B':'N.D.',
                'Cl':'N.D.', 'Cu':'N.D.', 'Fe':'N.D.', 'Mn':'N.D.', 'Mo':'N.D.', 'Zn':'N.D.', 'Ni':'N.D.'
                }


def validar_numero(v):
    if type(v) == Decimal or type(v) == float or type(v) == int:
        return True
    else:
        return False

def ppm_kg_ha(elemento_ppm, profundidad, densidad_aparente):
    #FORMULA kg/ha = ppm X Profundidad de muestreo (cm)X Densidad Aparente del Suelo (gr/cm3) X 0.1
    e = elemento_ppm
    p = profundidad
    da = densidad_aparente

    if validar_numero(e) == True and validar_numero(p) == True and validar_numero(da) == True:
        e = Decimal(e)
        p = Decimal(p)
        da = Decimal(da)
        res = e * p * da * Decimal(0.1)
        res = round(res, 2)
        return res
    else:
        return "N.D."


def aportacion_requerida(elemento_ppm, elemnto_nombre, cultivo, rendimiento, profundidad, densidad_aparente):
    Valor_Nulo = "N.D."
    e = elemento_ppm
    en = elemnto_nombre
    c = cultivo
    r = rendimiento
    p = profundidad
    da = densidad_aparente

    if type(c) == str and type(en) == str:
        cultivos_existentes = [
                                'Alfalfa', 'Arroz', 'Cacahuate', 'Canola', 'Caña de Azucar', 'Cebada', 'Cebolla', 
                                'Chile', 'Girasol', 'Jitomate', 'Lechuga', 'Maíz', 'Sorgo', 'Soya', 'Trigo'
                                ]
        elementos_existentes = [
                                'N', 'P', 'K', 'Ca', 'Mg', 'S', 'B', 'Cl', 'Cu', 'Fe', 'Mn', 'Mo', 'Zn', 'Ni'
                                ]
        
        if c in cultivos_existentes and en in elementos_existentes:
            if validar_numero(e) == True and validar_numero(r) == True and validar_numero(p) == True and validar_numero(da) == True:
                requerimientos = requerimiento_Nutrientes(c, r)
                kg_en_el_suelo = ppm_kg_ha(e, p, da)
                req_elemento = requerimientos[en]
                if req_elemento > kg_en_el_suelo:
                    aportacion = req_elemento - kg_en_el_suelo
                    return aportacion
                else:
                    return "-"
            else:
                 return Valor_Nulo
        else:
            return Valor_Nulo
    else:
        return Valor_Nulo
