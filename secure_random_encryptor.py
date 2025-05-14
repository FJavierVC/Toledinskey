# secure_random_encryptor.py

import random
import json
from g1.Atbash import atbash
from g1.Cesar import cifrado_cesar, descifrado_cesar
from g1.Cod_URL import codificar_url, decodificar_url
from g1.Rail_Fence import codificar_rail_fence, decodificar_rail_fence
from g1.ROT13 import rot13
from g1.Vigenere import vigenere_codificar, vigenere_decodificar

from g2.base16 import codificar_base16, decodificar_base16
from g2.base32 import codificar_base32, decodificar_base32
from g2.base64 import codificar_base64, decodificar_base64
from g2.base85 import codificar_base85, decodificar_base85

from g3.XOR import xor_codificar, xor_decodificar


# Diccionario de algoritmos con alias ocultos
ALIAS = {
    "VX": "vigenere",
    "B6": "base16",
    "B3": "base32",
    "B4": "base64",
    "B5": "base85",
    "XR": "xor",
    "A3": "atbash",
    "R3": "rot13",
    "CZ": "cesar",
    "UR": "url",
    "RF": "railfence",
}

ALIAS_INV = {v: k for k, v in ALIAS.items()}


# Registro de algoritmos con su tipo y funciones
ALGORITMOS = {
    "atbash": {
        "tipo": "texto",
        "codificar": atbash,
        "decodificar": atbash
    },
    "rot13": {
        "tipo": "texto",
        "codificar": rot13,
        "decodificar": rot13
    },
    "cesar": {
        "tipo": "texto",
        "codificar": lambda t: cifrado_cesar(t, 3),
        "decodificar": lambda t: descifrado_cesar(t, 3)
    },
    "vigenere": {
        "tipo": "texto",
        "codificar": lambda t: vigenere_codificar(t, 'key'),
        "decodificar": lambda t: vigenere_decodificar(t, 'key')
    },
    "url": {
        "tipo": "texto",
        "codificar": codificar_url,
        "decodificar": decodificar_url
    },
    "railfence": {
        "tipo": "texto",
        "codificar": lambda t: codificar_rail_fence(t, 3),
        "decodificar": lambda t: decodificar_rail_fence(t, 3)
    },
    "base16": {
        "tipo": "binario",
        "codificar": codificar_base16,
        "decodificar": decodificar_base16
    },
    "base32": {
        "tipo": "binario",
        "codificar": codificar_base32,
        "decodificar": decodificar_base32
    },
    "base64": {
        "tipo": "binario",
        "codificar": codificar_base64,
        "decodificar": decodificar_base64
    },
    "base85": {
        "tipo": "binario",
        "codificar": codificar_base85,
        "decodificar": decodificar_base85
    },
    "xor": {
        "tipo": "binario",
        "codificar": lambda t: xor_codificar(t, 'key'),
        "decodificar": lambda t: xor_decodificar(t, 'key')
    },
}


def secure_random_encrypt(texto_original):
    secuencia = random.sample(list(ALGORITMOS.keys()), 3)
    resultado = texto_original
    historial = []
    formato_actual = "texto"

    for algoritmo in secuencia:
        alg = ALGORITMOS[algoritmo]

        if formato_actual == "texto" and alg['tipo'] == "binario":
            resultado = resultado.encode('utf-8').hex()
            formato_actual = "binario"
        elif formato_actual == "binario" and alg['tipo'] == "texto":
            try:
                resultado = bytes.fromhex(resultado).decode('utf-8')
                formato_actual = "texto"
            except Exception:
                return (
                    None, f"Error convertir de binario a texto en {algoritmo}"
                )
        resultado = alg['codificar'](resultado)
        historial.append(ALIAS_INV[algoritmo])

    return resultado, historial


def secure_random_decrypt(texto_cifrado, historial):
    resultado = texto_cifrado
    pasos_real = [ALIAS[cod] for cod in historial]
    formato_actual = (
        "binario"
        if any(ALGORITMOS[alg]['tipo'] == 'binario' for alg in pasos_real)
        else "texto"
    )

    for algoritmo in reversed(pasos_real):
        alg = ALGORITMOS[algoritmo]

        if formato_actual == "texto" and alg['tipo'] == "binario":
            resultado = resultado.encode('utf-8').hex()
            formato_actual = "binario"
        elif formato_actual == "binario" and alg['tipo'] == "texto":
            try:
                resultado = bytes.fromhex(resultado).decode('utf-8')
                formato_actual = "texto"
            except Exception:
                return None

        resultado = alg['decodificar'](resultado)

    return resultado


def exportar_a_json(ruta_archivo, mensaje_cifrado, historial):
    datos = {
        "mensaje": mensaje_cifrado,
        "historial": historial
    }
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)


def importar_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        return datos.get("mensaje"), datos.get("historial")
