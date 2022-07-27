def CDT(usuario: str, capital: int, tiempo: int):
    porcentajeInteres = 0.03
    porcentajePerder = 0.02
    vlrIntereses = (capital * porcentajeInteres * tiempo)/12
    vlrPerder = capital * porcentajePerder
    if tiempo <= 2:
        vlrTotal = capital - vlrPerder
    elif tiempo > 2:
        vlrTotal = capital + vlrIntereses

    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} " \
           f"para un tiempo de {tiempo} meses es: {vlrTotal}"


print(CDT("AB1015", 1000000, 3))
print(CDT("ER3366", 5000000, 2))
