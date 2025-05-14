def vigenere_codificar(texto, clave):
    """
    Codifica un texto usando el cifrado Vigenère con la clave dada.
    Solo afecta letras; los demás caracteres se mantienen.
    """
    resultado = []
    clave = clave.lower()
    indice_clave = 0

    for char in texto:
        if char.isalpha():
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord('a')
            if char.isupper():
                resultado.append(chr((ord(char) - 65 + desplazamiento) % 26 + 65))
            else:
                resultado.append(chr((ord(char) - 97 + desplazamiento) % 26 + 97))
            indice_clave += 1
        else:
            resultado.append(char)

    return ''.join(resultado)

def vigenere_decodificar(texto_codificado, clave):
    """
    Decodifica un texto cifrado con el cifrado Vigenère usando la clave dada.
    """
    resultado = []
    clave = clave.lower()
    indice_clave = 0

    for char in texto_codificado:
        if char.isalpha():
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord('a')
            if char.isupper():
                resultado.append(chr((ord(char) - 65 - desplazamiento) % 26 + 65))
            else:
                resultado.append(chr((ord(char) - 97 - desplazamiento) % 26 + 97))
            indice_clave += 1
        else:
            resultado.append(char)

    return ''.join(resultado)

# mensaje = "Ataque al amanecer"
# clave = "clave"
# cifrado = vigenere_codificar(mensaje, clave)
# descifrado = vigenere_decodificar(cifrado, clave)
