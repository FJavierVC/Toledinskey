
from secure_random_encryptor import (
    secure_random_encrypt,
    secure_random_decrypt
)
if __name__ == "__main__":
    mensaje = "Este es un mensaje secreto para cifrar"
    print(f"Texto original:\n{mensaje}\n")

    cifrado, pasos = secure_random_encrypt(mensaje)

    if cifrado is None:
        print("❌ Error durante el proceso de cifrado.")
    else:
        print(f"🔐 Texto cifrado:\n{cifrado}")
        print(f"🔁 Algoritmos aplicados (en orden): {pasos}\n")

        descifrado = secure_random_decrypt(cifrado, pasos)

        if descifrado is None:
            print("❌ Error durante el descifrado.")
        else:
            print(f"✅ Texto descifrado:\n{descifrado}")
