def rot13(texto):
    """
    Codifica o decodifica un texto usando ROT13.
    Este cifrado es simétrico, por lo que aplicar dos veces ROT13 recupera el texto original.
    """
    resultado = []
    for char in texto:
        if char.isupper():
            resultado.append(chr((ord(char) - 65 + 13) % 26 + 65))
        elif char.islower():
            resultado.append(chr((ord(char) - 97 + 13) % 26 + 97))
        else:
            resultado.append(char)
    return ''.join(resultado)
# cifrado = rot13("Hola Mundo")
# descifrado = rot13(cifrado)  # ROT13 aplicado dos veces revierte el mensaje
