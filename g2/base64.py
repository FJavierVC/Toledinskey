import base64

def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    base64_bytes = base64.b64encode(texto_bytes)
    return base64_bytes.decode('utf-8')

def decodificar_base64(base64_texto):
    try:
        base64_bytes = base64_texto.encode('utf-8')
        texto_bytes = base64.b64decode(base64_bytes)
        return texto_bytes.decode('utf-8')
    except Exception as e:
        return f"Error al decodificar: {e}"