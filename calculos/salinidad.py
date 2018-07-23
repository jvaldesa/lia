from decimal import Decimal

def cationes(titulacionCaMg, normalidadEDTA, titulacionCa, alicuota, Na, K):
    titulacionCaMg = Decimal(titulacionCaMg)
    normalidadEDTA = Decimal(normalidadEDTA)
    titulacionCa = Decimal(titulacionCa)
    alicuota = Decimal(alicuota)
    Na = Decimal(Na)
    K = Decimal(K)
    """
    Ca + Mg  (meq/L) = (ml titulación Ca+Mg * Normalidad EDTA * 1000)/ml Alicuota
    Ca = ml titulación Ca
    Mg (meq/L) = (Ca + Mg  (meq/L)) - Ca
    Na (meq/L) = Na(ppm)/23   => peso equivalente de Na = 23
    k (meq/L) = Na(ppm)/39.1   => peso equivalente de Na = 39.1
    """
    CaMg = (titulacionCaMg * normalidadEDTA * Decimal(1000)) / alicuota
    Ca = titulacionCa
    Mg = CaMg -Ca
    Nameq = Na / Decimal(23)
    Kmeq = K / Decimal(39.1)

    Ca = round(Ca, 2)
    Mg = round(Mg, 2)
    Nameq = round(Nameq, 2)
    Kmeq = round(Kmeq, 2)

    return {'Ca': Ca, 'Mg':Mg, 'Na':Nameq, 'K':Kmeq}



def aniones(titulacionCar, titulacionBlancoCar, normalidadH2SO4, alicuotaCar, titulacionBic, titulacionBlancoBic, alicuotaBic, titulacionClo, titulacionBlancoClo, normalidadAgNO3, alicuotaClo, conductividadEl, unidad):
    titulacionCar = Decimal(titulacionCar)
    titulacionBlancoCar = Decimal(titulacionBlancoCar)
    normalidadH2SO4 = Decimal(normalidadH2SO4)
    alicuotaCar = Decimal(alicuotaCar)
    titulacionBic = Decimal(titulacionBic)
    titulacionBlancoBic = Decimal(titulacionBlancoBic)
    alicuotaBic = Decimal(alicuotaBic)
    titulacionClo = Decimal(titulacionClo)
    titulacionBlancoClo = Decimal(titulacionBlancoClo)
    normalidadAgNO3 = Decimal(normalidadAgNO3)
    alicuotaClo = Decimal(alicuotaClo)
    conductividadEl = Decimal(conductividadEl)

    if unidad == 'µS/cm':
        Ce = conductividadEl / 1000
    elif unidad == 'mS/cm':
        Ce = conductividadEl

    """
    x = Volumen gastado en titulación carbonatos - volumen gastado en titulación blanco carbonatos
    Carbonatos (meq/L) = (2 * x * Normalidad del H2SO4 * 1000) / mililitros de Alicuota Carbonatos
    y = Volumen gastado en titulación bicarbonatos - volumen gastado en titulación blanco bicarbonatos
    Bicarbonatos = (y - (2 * x) * Normalidad del H2SO4 * 1000) / mililitros de Alicuota Bicarbonatos
    z = volumen gastado en titulación cloruros - volumen gastado en titulación blanco cloruros
    Cloruros = (z * Normalidad AgNO3 * 1000) / mililitros de Alicuota Cloruros 
    Sulfatos = Conductividad electrica (mS/cm) * 10 -(Carbonatos + Bicarbonatos + Cloruros)
    """
    x = titulacionCar - titulacionBlancoCar
    y = titulacionBic - titulacionBlancoBic
    z = titulacionClo - titulacionBlancoClo

    Carbonatos = (2 * x * normalidadH2SO4 * 1000) / alicuotaCar
    Bicarbonatos = ((y - (2 * x)) * normalidadH2SO4 * 1000) / alicuotaBic
    Cloruros = (z * normalidadAgNO3 * 1000) / alicuotaClo
    Sulfatos = Ce * 10 -(Carbonatos + Bicarbonatos + Cloruros)

    Carbonatos = round(Carbonatos, 2)
    Bicarbonatos = round(Bicarbonatos, 2)
    Cloruros = round(Cloruros, 2)
    Sulfatos = round(Sulfatos, 2)

    return {'Carbonatos':Carbonatos, 'Bicarbonatos': Bicarbonatos, 'Cloruros': Cloruros, 'Sulfatos':Sulfatos}


