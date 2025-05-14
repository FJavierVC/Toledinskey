import urllib.parse

def codificar_url(texto):
    """
    Codifica un texto usando codificación URL (percent-encoding).
    """
    return urllib.parse.quote(texto)

def decodificar_url(texto_codificado):
    """
    Decodifica un texto desde codificación URL (percent-encoding).
    """
    try:
        return urllib.parse.unquote(texto_codificado)
    except Exception as e:
        return f"Error al decodificar: {e}"
