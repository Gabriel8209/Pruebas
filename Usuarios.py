import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

ventana = ctk.CTk()
ventana.title("Ventana de pureba")
ventana.geometry("300x200")

etiqueta = ctk.CTkLabel(ventana, text="Prueba 1", font=("Calibri", 16)) 
etiqueta.pack(pady=20)

boton = ctk.CTkButton(ventana, text="Botón", command=lambda: print("CLick"))
boton.pack(pady=10)

texto = ctk.CTkEntry(master=ventana, width= int(100), height= int(30), )
texto.pack(pady=30)
texto.pack(padx=500)
ventana.mainloop()