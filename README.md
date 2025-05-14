# 🔐 Toledisnkey

Toledisnkey es una aplicación de escritorio en Python diseñada para agregar una capa extra de seguridad en la comunicación de mensajes mediante cifrado múltiple y exportación segura de archivos.

Utiliza una interfaz gráfica moderna basada en `customtkinter`, con una experiencia optimizada para usuarios finales.

---

## 🎯 Objetivo del Proyecto

El objetivo principal de Toledisnkey es brindar una herramienta sencilla pero potente para **cifrar mensajes con múltiples algoritmos combinados** y facilitar su envío a través de medios digitales, especialmente mediante el uso de **archivos `.json` adjuntos en correos electrónicos seguros**.

El programa se enfoca en:
- Concientizar sobre la importancia del cifrado y la privacidad.
- Simular un entorno donde múltiples capas de cifrado protegen los datos.
- Demostrar la facilidad de cifrado + exportación + envío como flujo completo.

---

## 🔐 Características principales

- **Cifrado multilayer aleatorio** con historial de algoritmos aplicados.
- **Exportación en formato JSON** del mensaje cifrado junto con metadatos.
- **Importación y descifrado automático** desde archivo JSON válido.
- **Envío de mensajes cifrados por correo electrónico** utilizando App Password de Gmail.
- Interfaz **oscura estilo cyberpunk**, con icono y logo personalizados.
- **Scroll adaptativo** para pantallas pequeñas.
- Manejo de errores y rutas dinámicas (soporta cambios de ubicación del programa).

---

## ⚠️ Limitaciones

- El campo de texto está limitado a **20 caracteres máximo** para garantizar compatibilidad con los algoritmos de cifrado en capas.
- La aplicación está diseñada con fines **educativos y de demostración**, no como sistema de cifrado de grado militar.

---

## 🛠 Instrucciones de uso

1. Escribe un mensaje corto (máx. 20 caracteres) en el campo de entrada.
2. Haz clic en **Cifrar** para aplicar los algoritmos aleatorios.
3. Revisa los algoritmos aplicados en el historial.
4. Haz clic en **Exportar JSON** para guardar el mensaje cifrado.
5. Ingresa tu correo Gmail y app password como remitente.
6. Especifica el destinatario y usa el botón **Enviar** para transmitir el archivo cifrado.

---

## 📁 Estructura del proyecto

```
Toledisnkey/
├── gui.py
├── secure_random_encryptor.py
├── assets/
│   ├── icono.ico
│   └── logo.png
└── README.md
```

---

## ✉️ Nota sobre el correo

Para enviar correos desde una cuenta Gmail, deberás usar una **App Password** generada desde:  
[https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)  
(Si tienes autenticación de dos pasos activa).

---

## 📜 Licencia

Este proyecto fue desarrollado con fines educativos para demostrar la aplicación de múltiples técnicas de cifrado y su integración con flujos seguros de envío digital.
