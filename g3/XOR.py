def xor_codificar(texto, clave):
    """
    Codifica un texto usando cifrado XOR con una clave.
    Retorna una cadena de texto codificada como hexadecimal.
    """
    clave_bytes = clave.encode('utf-8')
    texto_bytes = texto.encode('utf-8')
    resultado = bytearray()

    for i in range(len(texto_bytes)):
        resultado.append(texto_bytes[i] ^ clave_bytes[i % len(clave_bytes)])

    return resultado.hex()

def xor_decodificar(texto_codificado_hex, clave):
    """
    Decodifica un texto cifrado con XOR (en formato hexadecimal) usando la misma clave.
    """
    clave_bytes = clave.encode('utf-8')
    texto_bytes = bytes.fromhex(texto_codificado_hex)
    resultado = bytearray()

    for i in range(len(texto_bytes)):
        resultado.append(texto_bytes[i] ^ clave_bytes[i % len(clave_bytes)])

    try:
        return resultado.decode('utf-8')
    except UnicodeDecodeError as e:
        return f"Error al decodificar: {e}"

# clave = "secreta"
# cifrado = xor_codificar("Mensaje secreto", clave)
# descifrado = xor_decodificar(cifrado, clave)
