from decimal import Decimal

def nitrogeno(M, B, N, Vi, a, p):
    M = Decimal(M)
    B = Decimal(B)
    N = Decimal(N)
    Vi = Decimal(Vi)
    a = Decimal(a)
    p = Decimal(p)

    Nppm = round((M - B) * N * Decimal(14) * (Vi / a) * (1 / p) * 1000, 2)
    return Nppm


def carbonatos(m, a, b, s):
    m = Decimal(m)
    a = Decimal(a)
    b = Decimal(b)
    s = Decimal(s)

    carbonatos = round(m * ((a - b) / s) * 50, 2)

    return carbonatos

