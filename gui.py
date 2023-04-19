import tkinter as tk
from tkinter import font
from time import sleep

window = tk.Tk()
window.resizable(False, False)
#window.geometry('400x500')

count = 2

class Application(tk.Frame):

    def __init__(self, master=window):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        # Tem de chamar esse método pra funcionar o width e o height do Frame
        # self.grid_propagate(False)
    
    # Tem que gerar dinamicamente isso aqui
    def create_input(self):

        global count
        count += 1  

        self.input_box = tk.Entry(self, bd=5)
        self.input_box.grid(column=0, row=count, padx=20)     

        self.input_box_2 = tk.Entry(self, bd=5)
        self.input_box_2.grid(column=1, row=count, padx=20)
        
        self.input_box_3 = tk.Entry(self, bd=5)
        self.input_box_3.grid(column=2, row=count, padx=20)

    # Aqui a gente realiza o cálculo
    def calcular(self):
        print('Estou calculando...')
        sleep(1)
        
        self.result = 0
        print(self.result)
        return self.result

    def createWidgets(self):

        self.text_g = tk.Label(self, text="Bagulho")
        self.text_g.grid(column=0, row=1)
        self.input_box = tk.Entry(self, bd=5)
        self.input_box.grid(column=0, row=2, padx=20)     

        self.text_g_2 = tk.Label(self, text="Bagulho")
        self.text_g_2.grid(column=1, row=1)
        self.input_box_2 = tk.Entry(self, bd=5)
        self.input_box_2.grid(column=1, row=2, padx=20)
        
        self.text_g_2 = tk.Label(self, text="Bagulho")
        self.text_g_2.grid(column=2, row=1)
        self.input_box_3 = tk.Entry(self, bd=5)
        self.input_box_3.grid(column=2, row=2, padx=20)

        self.titulo = tk.Label(self, text="Prop incerteza", font=('Courier', 15, 'bold'))
        self.titulo.grid(column=1, row=0, pady=30)

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', 
                                      command=self.calcular, font=("Courier", 16, 'bold'), fg='white', 
                                      relief='raised')
        self.calcular_btn.grid(column=1, row=40, pady=40)

app = Application()  
app.master.title('Prop incerteza')
app.mainloop()