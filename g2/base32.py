import base64

def codificar_base32(texto):
    """
    Codifica un texto en Base32.
    """
    texto_bytes = texto.encode('utf-8')
    base32_bytes = base64.b32encode(texto_bytes)
    return base32_bytes.decode('utf-8')

def decodificar_base32(base32_texto):
    """
    Decodifica un texto desde Base32.
    """
    try:
        base32_bytes = base32_texto.encode('utf-8')
        texto_bytes = base64.b32decode(base32_bytes)
        return texto_bytes.decode('utf-8')
    except Exception as e:
        return f"Error al decodificar: {e}"
