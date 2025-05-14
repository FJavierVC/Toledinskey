import base64

def codificar_base85(texto):
    """
    Codifica un texto en Base85 (ASCII85).
    """
    texto_bytes = texto.encode('utf-8')
    base85_bytes = base64.b85encode(texto_bytes)
    return base85_bytes.decode('utf-8')

def decodificar_base85(base85_texto):
    """
    Decodifica un texto desde Base85 (ASCII85).
    """
    try:
        base85_bytes = base85_texto.encode('utf-8')
        texto_bytes = base64.b85decode(base85_bytes)
        return texto_bytes.decode('utf-8')
    except Exception as e:
        return f"Error al decodificar: {e}"
