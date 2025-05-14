def codificar_rail_fence(texto, niveles):
    """
    Codifica un texto usando el cifrado Rail Fence con el número de niveles dado.
    """
    if niveles <= 1:
        return texto

    rieles = ['' for _ in range(niveles)]
    direccion = 1  # 1 para abajo, -1 para arriba
    riel_actual = 0

    for char in texto:
        rieles[riel_actual] += char
        riel_actual += direccion

        if riel_actual == 0 or riel_actual == niveles - 1:
            direccion *= -1  # Cambiar de dirección

    return ''.join(rieles)

def decodificar_rail_fence(texto_codificado, niveles):
    """
    Decodifica un texto cifrado con Rail Fence con el número de niveles dado.
    """
    if niveles <= 1:
        return texto_codificado

    # Paso 1: construir patrón del recorrido
    patron = [0] * len(texto_codificado)
    riel_actual = 0
    direccion = 1

    for i in range(len(texto_codificado)):
        patron[i] = riel_actual
        riel_actual += direccion
        if riel_actual == 0 or riel_actual == niveles - 1:
            direccion *= -1

    # Paso 2: contar cuántos caracteres van en cada riel
    conteo_rieles = [patron.count(n) for n in range(niveles)]

    # Paso 3: llenar los rieles con los caracteres del texto codificado
    rieles = []
    idx = 0
    for cantidad in conteo_rieles:
        rieles.append(list(texto_codificado[idx:idx + cantidad]))
        idx += cantidad

    # Paso 4: reconstruir el texto original usando el patrón
    resultado = []
    for riel in patron:
        resultado.append(rieles[riel].pop(0))

    return ''.join(resultado)
# mensaje = "ATAQUEINALUZ"
# cifrado = codificar_rail_fence(mensaje, 3)
# descifrado = decodificar_rail_fence(cifrado, 3)

