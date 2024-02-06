#el dialog promt se escribe "prompt", se almacena adentro de una variable y te pide un input
# nombre_de_la_variable = promt("titulo que aparece arriba", "aca pones el dato que queres q ponga el usuario")

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ignacio 
apellido: Taborda
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre_alumno = prompt("Datos", "Ingrese su nombre")
        alert("Datos", nombre_alumno)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()