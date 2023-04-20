import tkinter as tk
from tkinter import font
from time import sleep

window = tk.Tk()
window.resizable(False, False)
#window.geometry('400x500')

class ResultWindow(tk.Frame):
    result = float
    def __init__(self, master=window, result=result):
        self.result = result
        tk.Frame.__init__(self, master) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.titulo_result = tk.Label(self, text='Resultado: {}'.format(str(self.result)))
        self.titulo_result.grid()

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

        self.eq_input = tk.Entry(self, bd=5)
        self.eq_input.grid(column=0, row=count, padx=20)     

        self.var_input = tk.Entry(self, bd=5)
        self.var_input.grid(column=1, row=count, padx=20)
        
        self.stuff_input = tk.Entry(self, bd=5)
        self.stuff_input.grid(column=2, row=count, padx=20)

        # Adiciona numa DS pra realizar os cálculos
        # ...

    # Aqui a gente realiza o cálculo
    def calcular(self):
        print('Estou calculando...')
        sleep(1)
        
        self.result = 0
        print(self.result)

        # Abre a janela de resultado
        result_window = ResultWindow(result=self.result)
        result_window.master.title('Resultado')
        result_window.mainloop()

        return self.result

    def createWidgets(self):

        self.titulo = tk.Label(self, text="Prop incerteza", font=('Courier', 15, 'bold'))
        self.titulo.grid(column=1, row=0, pady=30)

        self.add_input_btn = tk.Button(self, text="+", background='green', 
                                      command=self.create_input, font=("Courier", 8, 'bold'), fg='white', 
                                      relief='flat')
        self.add_input_btn.grid(column=2, row=0)

        self.eq_text = tk.Label(self, text="Equação")
        self.eq_text.grid(column=0, row=1)
        self.eq_input = tk.Entry(self, bd=5)
        self.eq_input.grid(column=0, row=2, padx=20)     

        self.var_text = tk.Label(self, text="Variável")
        self.var_text.grid(column=1, row=1)
        self.var_input = tk.Entry(self, bd=5)
        self.var_input.grid(column=1, row=2, padx=20)
        
        self.stuff_text = tk.Label(self, text="Stuff")
        self.stuff_text.grid(column=2, row=1)
        self.stuff_input = tk.Entry(self, bd=5)
        self.stuff_input.grid(column=2, row=2, padx=20)

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', 
                                      command=self.calcular, font=("Courier", 16, 'bold'), fg='white', 
                                      relief='raised')
        self.calcular_btn.grid(column=1, row=40, pady=40)

app = Application()  
app.master.title('Prop incerteza')
app.mainloop()