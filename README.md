# 🔐 Toledisnkey

Toledisnkey es una aplicación de escritorio en Python diseñada para cifrar y descifrar mensajes con múltiples capas de encriptación, exportarlos en formato JSON y enviarlos por correo electrónico de forma segura. Utiliza una interfaz moderna con `customtkinter`.

---

## 🎨 Interfaz moderna
- Modo oscuro con acentos verdes (estilo cyberpunk).
- Logo personalizado y diseño responsivo.
- Campos integrados para remitente y destinatario.
- Scroll automático para pantallas pequeñas.

---

## 🧩 Características

- 🔒 Cifrado multilayer (algoritmos aleatorios)
- 📤 Exportación del mensaje cifrado en `.json`
- 📥 Importación y descifrado desde archivo
- 📧 Envío de archivo cifrado por correo Gmail
- 🖼 Interfaz con logo, scroll y botones estilizados

---

## 📦 Instalación

### Requisitos:

- Python 3.10 o superior
- Pip

### Dependencias:

```bash
pip install customtkinter pillow
```

También asegúrate de tener instalado el módulo de cifrado personalizado que viene con el proyecto:
- `secure_random_encryptor.py`

---

## 🚀 Ejecución

```bash
python gui3.py
```

---

## 📁 Estructura del proyecto

```
Toledisnkey/
├── gui3.py
├── secure_random_encryptor.py
├── assets/
│   ├── icono.ico
│   └── logo.png
└── README.md
```

---

## ✉️ Nota sobre el correo
Para enviar correos desde una cuenta Gmail, deberás usar una **App Password** generada desde [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)  
(Si tienes autenticación de dos pasos activa).

---

## 📜 Licencia
Este proyecto fue desarrollado con fines educativos y de demostración de cifrado seguro.
