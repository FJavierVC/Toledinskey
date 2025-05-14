def cifrado_cesar(texto, desplazamiento):
    """
    Codifica un texto usando el cifrado César con el desplazamiento dado.
    Mantiene mayúsculas, minúsculas y deja los caracteres no alfabéticos sin cambio.
    """
    resultado = []
    for char in texto:
        if char.isupper():
            resultado.append(chr((ord(char) - 65 + desplazamiento) % 26 + 65))
        elif char.islower():
            resultado.append(chr((ord(char) - 97 + desplazamiento) % 26 + 97))
        else:
            resultado.append(char)
    return ''.join(resultado)

def descifrado_cesar(texto, desplazamiento):
    """
    Decodifica un texto cifrado con el cifrado César usando el desplazamiento dado.
    """
    return cifrado_cesar(texto, -desplazamiento)

#SUGERENCIA PARA DESPLAZAMIENTO=3 PARA CIFRAR 