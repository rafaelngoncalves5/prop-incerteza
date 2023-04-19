import tkinter as tk
from tkinter import font

window = tk.Tk()
window.resizable(False, False)
window.geometry('400x500')

class Application(tk.Frame):
    def __init__(self, master=window):
        tk.Frame.__init__(self, master)
        self.grid()
        
        self.createWidgets()
        # Tem de chamar esse método pra funcionar o width e o height do Frame
        # self.grid_propagate(False)

    # Aqui a gente realiza o cálculo
    def calcular(self):
        print('Estou calculando...')

    def createWidgets(self):

        self.titulo = tk.Label(self, font=('Courier', 15, 'bold'), text="Prop incerteza", justify='center')
        self.titulo.grid(column=1, row=0, pady=20)

        self.input_box = tk.Entry(self)
        self.input_box.grid(column=0, row=1, padx=5)

        self.input_box_2 = tk.Entry(self)
        self.input_box_2.grid(column=1, row=1)

        self.input_box_3 = tk.Entry(self, width=5)
        self.input_box_3.grid(column=2, row=1)

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', justify=tk.CENTER, 
                                      command=self.calcular, font=("Courier", 16, 'bold'), fg='white', 
                                      relief='raised')
        self.calcular_btn.grid(column=1)

app = Application()  
app.master.title('Prop incerteza')
app.mainloop()