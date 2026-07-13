import customtkinter as ctk

# 1. Configuración de la apariencia general
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

# 2. Crear la instancia de la ventana principal
ventana = ctk.CTk()

# 3. Personalizar las propiedades de la ventana
ventana.title("Interfaz con Plano Cartesiano (.place)") 
ventana.geometry("450x400")                 
ventana.resizable(False, False) # Desactivamos el redimensionado para que tus coordenadas fijas no se desordenen

# 4. Definir las funciones
def mostrar_saludo():
    nombre_usuario = cuadro_texto.get()
    if nombre_usuario.strip() != "":
        etiqueta_bienvenida.configure(text=f"¡Hola, {nombre_usuario}!\nBienvenido/a a tu interfaz.")
    else:
        etiqueta_bienvenida.configure(text="Por favor, escribe tu nombre abajo.")

# 5. Crear los elementos gráficos
# Etiqueta de texto
etiqueta_bienvenida = ctk.CTkLabel(
    ventana, 
    text="¿Cómo te llamas?", 
    font=("Arial", 18, "bold")
)

# Cuadro de texto
cuadro_texto = ctk.CTkEntry(
    ventana, 
    placeholder_text="Escribe tu nombre aquí...",  
    width=250,                                    
    height=40,                                    
    corner_radius=8                               
)

# Botón interactivo
boton_accion = ctk.CTkButton(
    ventana, 
    text="Enviar", 
    command=mostrar_saludo,
    corner_radius=8
)

# Etiqueta pequeña decorativa
etiqueta_pie = ctk.CTkLabel(
    ventana, 
    text="Presiona 'X' en la esquina para cerrar", 
    font=("Arial", 10, "italic"),
    text_color="gray"
)

# --- UBICACIÓN CON EL PLANO CARTESIANO (.place) ---
# Usamos 'anchor="center"' para que la coordenada que le demos sea el centro exacto del objeto.

# Colocamos la etiqueta de bienvenida arriba en el centro
# X = 225 (mitad de la ventana que mide 450)
# Y = 80 (cerca de la parte superior)
etiqueta_bienvenida.place(x=225, y=80, anchor="center")

# Colocamos el cuadro de texto justo en el centro de la pantalla
# X = 225 (mitad del ancho)
# Y = 180 (un poco arriba del centro vertical)
cuadro_texto.place(x=225, y=180, anchor="center")

# Colocamos el botón un poco más abajo del cuadro de texto
# X = 225 (alineado en el centro horizontal)
# Y = 260 (más abajo que el cuadro de texto)
boton_accion.place(x=225, y=260, anchor="center")

# Colocamos el pie de página cerca del borde inferior
# X = 225 (centro horizontal)
# Y = 360 (muy cerca del final de la ventana de 400 de alto)
etiqueta_pie.place(x=225, y=360, anchor="center")

# 6. Iniciar el bucle de eventos principal
ventana.mainloop()