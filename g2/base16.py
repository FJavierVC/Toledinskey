import base64

def codificar_base16(texto):
    """
    Codifica un texto en Base16 (hexadecimal).
    """
    texto_bytes = texto.encode('utf-8')
    base16_bytes = base64.b16encode(texto_bytes)
    return base16_bytes.decode('utf-8')

def decodificar_base16(base16_texto):
    """
    Decodifica un texto desde Base16 (hexadecimal).
    """
    try:
        base16_bytes = base16_texto.encode('utf-8')
        texto_bytes = base64.b16decode(base16_bytes)
        return texto_bytes.decode('utf-8')
    except Exception as e:
        return f"Error al decodificar: {e}"
