import customtkinter as ctk

ventana = ctk.CTk()
ventana.title("Prueba con .grid()")
ventana.geometry("500x300")

# Configuramos la cuadrícula para que esté centrada en la ventana
ventana.grid_columnconfigure((0, 1), weight=1)

# Fila 0, Columna 0 (Izquierda)
etiqueta = ctk.CTkLabel(ventana, text="Tu nombre:", font=("Arial", 14))
etiqueta.grid(row=0, column=0, padx=10, pady=20)

# Fila 0, Columna 1 (Derecha, al lado de la etiqueta)
cuadro_texto = ctk.CTkEntry(ventana, placeholder_text="Escribe aquí...")
cuadro_texto.grid(row=0, column=1, padx=10, pady=20)

# Fila 1. Usamos columnspan=2 para que el botón se centre ocupando ambas columnas
boton = ctk.CTkButton(ventana, text="Enviar")
boton.grid(row=1, column=0, columnspan=2, pady=20)

ventana.mainloop()