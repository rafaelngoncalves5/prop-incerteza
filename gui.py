import tkinter as tk
from tkinter import font
import test

class ResultWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.titulo = tk.Label(self, font=('Courier', 20, 'bold'), text="Resultado", pady=30)
        self.titulo.grid()


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    # Aqui a gente realiza o cálculo
    def calcular(self):
        print('Estou calculando...')
        for f in font.families():
            print(f)

        # Instancio uma janela com o resultado
        rw = ResultWindow()                     
        rw.master.title('Resultado')
        rw.mainloop()

    def createWidgets(self):

        self.titulo = tk.Label(self, font=('Courier', 20, 'bold'), text="Prop incerteza", pady=30)
        self.titulo.grid()

        self.input_box = tk.Entry(self, width=25)
        self.input_box.grid()

        self.input_box_2 = tk.Entry(self, width=25)
        self.input_box_2.grid()

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', justify=tk.CENTER, 
                                      command=self.calcular, font=("Courier", 16, 'bold'), fg='white', 
                                      relief='raised', width=25)
        self.calcular_btn.grid()

app = Application()                     
app.master.title('Prop incerteza')
app.mainloop()