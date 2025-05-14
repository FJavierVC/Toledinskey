def atbash(texto):
    """
    Codifica o decodifica un texto usando el cifrado Atbash.
    El cifrado Atbash es simétrico, por lo que codificar y decodificar es lo mismo.
    """
    resultado = []
    for char in texto:
        if char.isalpha():
            if char.isupper():
                # A-Z → Z-A
                resultado.append(chr(65 + (25 - (ord(char) - 65))))
            else:
                # a-z → z-a
                resultado.append(chr(97 + (25 - (ord(char) - 97))))
        else:
            # Caracter no alfabético se deja igual
            resultado.append(char)
    return ''.join(resultado)

# Uso:
# codificado = atbash("Hola Mundo")
# decodificado = atbash(codificado)  # Atbash es simétrico
