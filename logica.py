def capturarSimbolos(texto):
    resultado = ""
    longitud = len(texto)

    for i in range(longitud):
        codigo_ascii = ord(texto[i])
        if (codigo_ascii >= 33 and codigo_ascii <= 47) or (codigo_ascii >= 58 and codigo_ascii <= 64) or (codigo_ascii >= 123 and codigo_ascii <= 255):
            resultado = resultado + texto[i]


    return resultado

def capturarCaracteres(texto):
    resultado = ""
    longitud = len(texto)

    for i in range(longitud):
        codigo_ascii = ord(texto[i])
        if (codigo_ascii >= 65 and codigo_ascii <= 122):
            resultado = resultado + texto[i]


    return resultado

def capturarNumeros(texto):
    resultado = ""
    longitud = len(texto)

    for i in range(longitud):
        codigo_ascii = ord(texto[i])
        if (codigo_ascii >= 48 and codigo_ascii <= 57):
            resultado = resultado + texto[i]


    return resultado