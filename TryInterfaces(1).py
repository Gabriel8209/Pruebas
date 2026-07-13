import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

ventana = ctk.CTk()

ventana.title("Prueba de una ventana. ¡Hola!")
ventana.geometry("450x400")
ventana.wm_resizable(False, False)

def mostrar_saludo():
    nombre_usuario = cuadro_texto.get()
    if nombre_usuario.strip() != "":
        etiqueta_bienvenida.configure(text=f"Hola, {nombre_usuario} \nBienvenido a tu interfaz.")
    else:
        etiqueta_bienvenida.configure(text="Por favor, escribe tu nombre aquí abajo")


etiqueta_bienvenida = ctk.CTkLabel(ventana, text="Cómo te llamas?", text_color="orange", font=("Arial", 30, "bold"))
etiqueta_bienvenida.pack(side="top", pady=10)

cuadro_texto = ctk.CTkEntry(ventana, placeholder_text="Escribe tu nombre aquí...", width=250, height=40, corner_radius=8)
cuadro_texto.pack(side="top", pady=20)

boton_accion = ctk.CTkButton(ventana, text="Enviar>>>", command=mostrar_saludo, corner_radius=8)
boton_accion.pack(side="top", pady=20)

etiqueta_pie = ctk.CTkLabel(ventana, text="Preciona la 'X' de arriba a la derecha para salir", font=("Arial", 10, "italic"), text_color="red")
etiqueta_pie.pack(side="bottom", pady=20)


ventana.mainloop()
