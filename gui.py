import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image
from secure_random_encryptor import (
    secure_random_encrypt,
    secure_random_decrypt,
    exportar_a_json,
    importar_desde_json
)
import smtplib
from email.message import EmailMessage
import os

# Configurar tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Ventana principal
app = ctk.CTk()
app.title("Toledisnkey")
app.geometry("800x700")

# Icono dinámico seguro
icon_path = os.path.join(os.path.dirname(__file__), "assets", "icono.ico")
if os.path.exists(icon_path):
    app.iconbitmap(icon_path)

# Scrollable Frame principal
scrollable_frame = ctk.CTkScrollableFrame(app)
scrollable_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Logo al centro
logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
if os.path.exists(logo_path):
    logo_img = ctk.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(120, 120)
    )
    logo_label = ctk.CTkLabel(scrollable_frame, image=logo_img, text="")
    logo_label.pack(pady=(10, 20))

# Variables globales
historial_actual = []
remitente_actual = ""
clave_actual = ""
# Funciones

def guardar_remitente():
    global remitente_actual, clave_actual
    remitente_actual = entry_remitente.get()
    clave_actual = entry_clave.get()
    if remitente_actual and clave_actual:
        messagebox.showinfo("Configuración", "Remitente guardado correctamente.")
        log_resultado.configure(text=f"✅ Remitente configurado: {remitente_actual}")
    else:
        messagebox.showwarning("Campos vacíos", "Ingresa ambos campos de remitente.")

def cifrar():
    global historial_actual
    texto = input_text.get("1.0", "end").strip()
    if not texto:
        messagebox.showwarning("Advertencia", "El texto no puede estar vacío.")
        return
    cifrado, historial = secure_random_encrypt(texto)
    historial_actual = historial
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", cifrado)
    output_text.configure(state="disabled")
    algo_result.configure(text=" → ".join(historial))
    input_text.delete("1.0", "end")
    log_resultado.configure(text="Texto cifrado exitosamente.")

def exportar():
    if not historial_actual:
        messagebox.showwarning("Advertencia", "No hay datos para exportar.")
        return
    texto_cifrado = output_text.get("1.0", "end").strip()
    ruta = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivo JSON", "*.json")])
    if ruta:
        exportar_a_json(ruta, texto_cifrado, historial_actual)
        messagebox.showinfo("Exportado", f"Mensaje exportado a: {ruta}")
        log_resultado.configure(text="Archivo JSON exportado correctamente.")

def importar():
    ruta = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
    if ruta:
        mensaje, historial = importar_desde_json(ruta)
        if mensaje and historial:
            descifrado = secure_random_decrypt(mensaje, historial)
            input_text.delete("1.0", "end")
            input_text.insert("end", descifrado)
            output_text.configure(state="normal")
            output_text.delete("1.0", "end")
            output_text.insert("end", mensaje)
            output_text.configure(state="disabled")
            algo_result.configure(text=" → ".join(historial))
            log_resultado.configure(text="Archivo importado y descifrado exitosamente.")
        else:
            messagebox.showerror("Error", "El archivo no contiene datos válidos.")

def enviar_email():
    global historial_actual
    correo_destino = entry_destinatario.get()
    if not historial_actual:
        messagebox.showwarning("Advertencia", "Primero cifra y exporta el mensaje.")
        return
    if not remitente_actual or not clave_actual:
        messagebox.showwarning("Configuración", "Primero configura el correo del remitente.")
        return
    if not correo_destino:
        messagebox.showwarning("Falta destinatario", "Ingresa el correo de destino.")
        return
    ruta = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
    if not ruta or not os.path.exists(ruta):
        return
    try:
        msg = EmailMessage()
        msg["Subject"] = "Mensaje cifrado - Toledisnkey"
        msg["From"] = remitente_actual
        msg["To"] = correo_destino
        msg.set_content("Adjunto archivo JSON con el mensaje cifrado.")
        with open(ruta, "rb") as f:
            contenido = f.read()
            msg.add_attachment(contenido, maintype="application", subtype="json", filename=os.path.basename(ruta))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(remitente_actual, clave_actual)
            smtp.send_message(msg)
        messagebox.showinfo("Enviado", "Correo enviado correctamente.")
        log_resultado.configure(text=f"Correo enviado desde {remitente_actual} a {correo_destino} ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo:\n{e}")
        log_resultado.configure(text="❌ Error al enviar el correo.")

# Layout principal sobre scrollable_frame
label_input = ctk.CTkLabel(scrollable_frame, text="Texto original:")
label_input.pack(pady=(10, 0))

input_text = ctk.CTkTextbox(scrollable_frame, height=100)
input_text.pack(padx=10, pady=5, fill="x")

label_output = ctk.CTkLabel(scrollable_frame, text="Texto cifrado:")
label_output.pack(pady=(10, 0))

output_text = ctk.CTkTextbox(scrollable_frame, height=100, state="disabled")
output_text.pack(padx=10, pady=5, fill="x")

label_algos = ctk.CTkLabel(scrollable_frame, text="Algoritmos aplicados:")
label_algos.pack(pady=(10, 0))

algo_result = ctk.CTkLabel(scrollable_frame, text="")
algo_result.pack(pady=2)

log_resultado = ctk.CTkLabel(scrollable_frame, text="")
log_resultado.pack(pady=5)

# Sección de botones principales
ctk.CTkButton(scrollable_frame, text="Cifrar", width=200, command=cifrar).pack(pady=5)

botones_linea = ctk.CTkFrame(scrollable_frame)
botones_linea.pack(pady=10)
ctk.CTkButton(botones_linea, text="Exportar JSON", width=200, command=exportar).pack(side="left", padx=10)
ctk.CTkButton(botones_linea, text="Importar y Descifrar JSON", width=200, command=importar).pack(side="left", padx=10)

# Sección de remitente
remitente_frame = ctk.CTkFrame(scrollable_frame)
remitente_frame.pack(pady=10, fill="x")
ctk.CTkLabel(remitente_frame, text="Datos del remitente:").pack(anchor="w", padx=10)
entry_remitente = ctk.CTkEntry(remitente_frame, placeholder_text="Correo Gmail")
entry_remitente.pack(padx=10, pady=5, fill="x")
entry_clave = ctk.CTkEntry(remitente_frame, placeholder_text="App Password", show="*")
entry_clave.pack(padx=10, pady=5, fill="x")
ctk.CTkButton(remitente_frame, text="Guardar", command=guardar_remitente).pack(pady=5)

# Sección de destinatario
destino_frame = ctk.CTkFrame(scrollable_frame)
destino_frame.pack(pady=10, fill="x")
ctk.CTkLabel(destino_frame, text="Correo del destinatario:").pack(anchor="w", padx=10)
entry_destinatario = ctk.CTkEntry(destino_frame, placeholder_text="Correo del destinatario")
entry_destinatario.pack(padx=10, pady=5, fill="x")
ctk.CTkButton(destino_frame, text="Enviar", command=enviar_email).pack(pady=5)

# Ejecutar
app.mainloop()
