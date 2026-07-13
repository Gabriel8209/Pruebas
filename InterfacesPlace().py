import customtkinter as ctk

ventana = ctk.CTk()
ventana.title("Prueba con .pack()")
ventana.geometry("450x400")

# Aquí ya no necesitamos coordenadas fijas
etiqueta = ctk.CTkLabel(ventana, text="¿Cómo te llamas?", font=("Arial", 18, "bold"))
# side="top" lo pone arriba, pady=20 le da espacio vertical para que respire
etiqueta.pack(side="top", pady=20)

cuadro_texto = ctk.CTkEntry(ventana, placeholder_text="Escribe tu nombre aquí...", width=250)
cuadro_texto.pack(side="top", pady=100)

boton = ctk.CTkButton(ventana, text="Enviar>>>")
boton.pack(side="top", pady=20)

etiqueta_pie = ctk.CTkLabel(ventana, text="Presiona la 'X' para salir", text_color="red")
# Lo mandamos al fondo de la ventana
etiqueta_pie.pack(side="bottom", pady=20)

etiqueda_segunda = ctk.CTkLabel(ventana, text="Este es un cuadro de \ntexto para probar", text_color="green", font=("Times New Roman", 20, "italic"))
etiqueda_segunda.pack(side="right", pady=30, padx=5)
ventana.mainloop()