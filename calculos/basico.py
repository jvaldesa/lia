from decimal import Decimal

def textura(l1, l2, l3, l4, t1, t2, t3, t4):
    pl = Decimal((l1 + l2 + l3) / 3)
    pt = Decimal((t1 + t2 + t3) / 3)
    vT1 = Decimal((pt - Decimal(19.5)) * Decimal(0.36))
    vT2 = Decimal((t4 - Decimal(19.5)) * Decimal(0.36))
    arenas = round(Decimal((100 - ((pl + vT1) * 2))), 2)
    arcillas = round(Decimal(((l4 + vT2) * 2)), 2)
    limos = round(Decimal((100 - (arenas + arcillas))),2)

    if (limos + Decimal(1.5) * arcillas) < 15:
        textura_r = "ARENOSA"
    elif ((limos + Decimal(1.5) * arcillas) >= 15) and ((limos + 2 * arcillas) < 30):
        textura_r = "ARENO FRANCOSA"
    elif ((arcillas >= 7 and arcillas < 27) and (limos >= 28 and limos < 50) and (arenas <= 52)):
        textura_r = "FRANCOSAS" 
    elif ((limos >= 50 and (arcillas >= 12 and arcillas < 27)) or ((limos >= 50 and limos < 80) and arcillas < 12)):
        textura_r = "FRANCO LIMOSA"
    elif (limos >= 80 and arcillas < 12):
        textura_r = "LIMOSA"
    elif ((arcillas >= 20 and arcillas < 35) and (limos < 28) and (arenas > 45)):
        textura_r = "FRANCO ARCILLO ARENOSA"
    elif ((arcillas >= 27 and arcillas < 40) and (arenas > 20 and arenas <= 45)):
        textura_r = "FRANCO ARCILLOSA"
    elif ((arcillas >= 27 and arcillas < 40) and (arenas <= 20)):
        textura_r = "FRANCO ARCILLO LIMOSA"
    elif (arcillas >= 35 and arenas > 45):
        textura_r = "ARCILLO ARENOSA"
    elif (arcillas >= 40 and limos >= 40):
        textura_r = "ARCILLO LIMOSA"
    elif (arcillas >= 40 and arenas <= 45 and limos < 40):
        textura_r = "ARCILLA"
    

    resultados = {'arenas': arenas, 'arcillas': arcillas, 'limos': limos, 'textura': textura_r}
    return resultados


def ph(ph):
    ph = Decimal(ph)

    if ph <= 5:
        clasificacion = "Fuertemente ácido"
    elif ph > 5 and ph <= 6.5:
        clasificacion = "Moderadamente ácido"
    elif ph > 6.5 and ph <= 7.3:
        clasificacion = "Neutro"
    elif ph > 6.3 and ph <= 8.5:
        clasificacion = "Medianamente alcalino"
    elif ph > 8.5:
        clasificacion = "Fuertemente alcalino"

    return clasificacion    


def conductividadElectrica(ce, unidad):
    ce = Decimal(ce)
    # unidad a = µS/cm
    # unidad b = mS/cm
    if unidad == 'µS/cm':
        Ec = ce / 1000
    elif unidad == 'mS/cm':
        Ec = ce
    
    if Ec <= 1:
        clasificacion = "Efectos despreciables de la salinidad"
    elif Ec > 1 and Ec <= 2:
        clasificacion = "Muy ligeramente salino"
    elif Ec > 2 and Ec <= 4:
        clasificacion = "Moderadamente salino"
    elif Ec > 4 and Ec <= 8:
        clasificacion = "Suelo salino"
    elif Ec > 8 and Ec <= 16:
        clasificacion = "Suelo salino"
    elif Ec > 16:
        clasificacion = "Muy fuertemente salino"
    
    return clasificacion


def materiaOrganica(clase_suelo, b1, b2, b3, t, g, N):
    promedioB = Decimal((b1 + b2 + b3 ) / 3)

    CarbonoOrganico = Decimal(((promedioB - Decimal(t)) / Decimal(g)) * Decimal(N) * Decimal(0.39))
    MateriaOrganica = round(Decimal(CarbonoOrganico * Decimal(1.7241)),2)

    if clase_suelo == 'Suelos volcánicos':
        if MateriaOrganica <= 4:
            clasificacion = 'Muy bajo'
        elif MateriaOrganica > 4 and MateriaOrganica <= 6:
            clasificacion = 'Bajo'
        elif MateriaOrganica > 6 and MateriaOrganica < 11:
            clasificacion = 'Medio'
        elif MateriaOrganica >= 11 and MateriaOrganica <= 16:
            clasificacion = 'Alto'
        elif MateriaOrganica > 16:
            clasificacion = 'Muy Alto'
    elif clase_suelo == 'Suelos no volcánicos':
        if MateriaOrganica <= Decimal(0.5):
            clasificacion = 'Muy bajo'
        elif MateriaOrganica > Decimal(0.5) and MateriaOrganica <= Decimal(1.5):
            clasificacion = 'Bajo'
        elif MateriaOrganica > Decimal(1.5) and MateriaOrganica <= Decimal(3.5):
            clasificacion = 'Medio'
        elif MateriaOrganica > Decimal(3.5) and MateriaOrganica <= 6:
            clasificacion = 'Alto'
        elif MateriaOrganica > 6:
            clasificacion = 'Muy Alto'

    return {'MO':MateriaOrganica, 'clasificacion':clasificacion}


def densidadAparente(PesoMuestra, VolumenMuestra):
    pm = Decimal(PesoMuestra)
    vm = Decimal(VolumenMuestra)
    DensidadAparente = round(pm / vm, 2)

    return DensidadAparente


def puntoSaturacion(PesoInicialEstufa, PesoFinalEstufa, AguaGastadaEstufa, PesoInicialAire, PesoFinalAire, AguaGastadaAire):
    peso_inicial_estufa = Decimal(PesoInicialEstufa)
    peso_final_estufa = Decimal(PesoFinalEstufa)
    agua_gastada_estufa = Decimal(AguaGastadaEstufa)
    peso_inicial_aire = Decimal(PesoInicialAire)
    peso_final_aire = Decimal(PesoFinalAire)
    agua_gastada_aire = Decimal(AguaGastadaAire)

    # Phu = Porciento de Humedad
    Phu = ((peso_inicial_estufa - peso_final_estufa) / peso_final_estufa) * 100
    punto_saturacion = round((((agua_gastada_aire + (peso_inicial_aire - peso_final_aire)) * 100) * (100 + Phu)) / (peso_final_aire * 100), 2)
    capacidad_campo = round(punto_saturacion * Decimal(0.75), 2)
    punto_marchitez_permanente = round((capacidad_campo / 2) + 5, 2)

    return {'PS': punto_saturacion, 'CC': capacidad_campo, 'PMP': punto_marchitez_permanente}