import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()

ventana.title("Prueba de interfaces 2")
ventana.geometry("500x650")

cuadro = ctk.CTkFrame(ventana, fg_color="transparent", border_width=2, )

titulo = ctk.CTkLabel(ventana, text="Bienvenido a esta interfaz de segunda prueba", text_color="white", font=("Calibri", 40, "italic"))
titulo.pack(side="top", anchor="w", pady=20, padx=10)

boton1 = ctk.CTkButton(ventana, text="Menú principal", height=200, width=200, fg_color="transparent", border_width=1, border_color="white")
boton1.pack(side="left", anchor="n", pady=20)

boton2 = ctk.CTkButton(ventana, text="Misiones", height=200, width=200, fg_color="transparent", border_width=1, border_color="white")
boton2.pack(side="left", anchor="n", pady=20)

boton2 = ctk.CTkButton(ventana, text="Equipamiento", height=200, width=200, fg_color="transparent", border_width=1, border_color="white")
boton2.pack(side="left", anchor="n", pady=20)

boton4 = ctk.CTkButton(ventana, text="Tienda", height=200, width=200, fg_color="transparent", border_width=1, border_color="white")
boton4.pack(side="left", anchor="n", pady=20)

boton5 = ctk.CTkButton(ventana, text="Configuración", height=200, width=200, fg_color="transparent", border_width=1, border_color="white")
boton5.pack(side="left", anchor="n", pady=20)

boton6 = ctk.CTkButton(ventana, text="Salir", height=200, width=200, fg_color="transparent", border_width=1, border_color="white")
boton6.pack(side="left", anchor="n", pady=20)

ventana.mainloop()