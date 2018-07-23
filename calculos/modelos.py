
def filtrarModeloconModelo(mPrincipal, mFiltro):
    queryPrincipal = mPrincipal.objects.all()
    queryFiltrado = mPrincipal.objects.all()
    queryFiltro = mFiltro.objects.all()

    for registro in queryPrincipal:
        for elemento in queryFiltro:
            if registro.id == elemento.folio_id:
                queryFiltrado = queryFiltrado.exclude(pk=registro.id)
    
    return queryFiltrado

