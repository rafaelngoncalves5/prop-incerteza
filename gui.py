import tkinter as tk
from tkinter import font
from time import sleep

var_list = list()
val_list = list()
inc_list = list()

svar_list = list()
sval_list = list()
sinc_list = list()

def calcular(equation, **kwargs):
    # Pegando a equação. Só existe uma equação
    print(equation)
    # Variáveis(var), valores(val) e incertezas(inc)
    print(kwargs)

    # Limpa a lista
    var_list.clear()
    val_list.clear()
    inc_list.clear()

class ResultWindow(tk.Frame):
    result = str
    latex = str

    def __init__(self, master=None, result=result, latex = latex):
        self.result = result
        self.latex = latex
        tk.Frame.__init__(self, master, background='grey') 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.titulo_result = tk.Label(self, foreground='white', background='grey', text="Resultado", font=('Courier', 15, 'bold'))
        self.titulo_result.grid(column=1, row=0, pady=30)

        self.show_result = tk.Label(self, text=str(self.result), font=('Courier', 12, 'bold'), 
                                    background='cyan', padx=20, pady=20)
        self.show_result.grid(column=1, row=1)

        self.titulo_latex = tk.Label(self, foreground='white', background='grey', text="Latex", font=('Courier', 15, 'bold'))
        self.titulo_latex.grid(column=1, row=2, pady=30)

        self.show_latex = tk.Label(self, text=str(self.result), font=('Courier', 12, 'bold'), 
                                    background='orange', padx=20, pady=20)
        self.show_latex.grid(column=1, row=3)

count = 5

window = tk.Tk()
window.resizable(False, False)
#window.geometry('400x500')

class Application(tk.Frame):

    def __init__(self, master=window):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        # Tem de chamar esse método pra funcionar o width e o height do Frame
        # self.grid_propagate(False)

    def grab_value(self):

        # Insere na lista de variáveis
        var_list.append(self.var_input.get())

        # Insere na lista de valores
        val_list.append(self.val_input.get())

        # Insere na lista de incertezas
        inc_list.append(self.inc_input.get())
        
        # Salva tudo
        for variable in svar_list:
            var_list.append(variable.get())

        for value in sval_list:
            val_list.append(value.get())

        for uncertainty in sinc_list:
            inc_list.append(uncertainty.get())

        # Realiza o cálculo em si:
        calcular(
            equation=self.eq_input.get(),
            var=var_list, 
            val=val_list,
            inc=inc_list,
            )

        # Retorna o resultado
        self.result = 'dsf32423423942034023042dvbv453443dsfsd343423tvb'

        self.latex = 'dfinsdkfnsdfngfkfgn'

        # Abre a janela de resultado
        res_window = tk.Tk()
        res_window.resizable(False, False)
        result_window = ResultWindow(master=res_window, result=self.result, latex=self.latex)
        result_window.master.title('Resultado')
        result_window.mainloop()

        # return self.result + self.latex

    def create_input(self):
        global count
        count += 1
         
        self.var1 = tk.Entry(self, bd=5)
        self.var1.grid(column=0, row=count, padx=20)

        self.val1 = tk.Entry(self,bd=5)
        self.val1.grid(column=1, row=count)

        self.inc1 = tk.Entry(self,bd=5)
        self.inc1.grid(column=2, row=count)

        svar_list.append(self.var1)
        sval_list.append(self.val1)
        sinc_list.append(self.inc1)


    def createWidgets(self):

        self.titulo = tk.Label(self, text="Prop incerteza", font=('Courier', 15, 'bold'))
        self.titulo.grid(column=1, row=0, pady=30)

        self.eq_text = tk.Label(self, text="Equação", font=('Courier', 12)).grid(column=1, row=1)
        self.eq_input = tk.Entry(self, bd=5)
        self.eq_input.grid(column=1, row=2)

        self.add_input_btn = tk.Button(self, text="+", background='green', 
                                      command=self.create_input, fg='white', 
                                      relief='flat', padx=5)
        self.add_input_btn.grid(column=1, row=39)

        self.var_text = tk.Label(self, text="Variável")
        self.var_text.grid(column=0, row=3)
        self.var_input = tk.Entry(self, bd=5)
        self.var_input.grid(column=0, row=4, padx=20)

        self.val_text = tk.Label(self, text="Valor")
        self.val_text.grid(column=1, row=3)
        self.val_input = tk.Entry(self, bd=5)
        self.val_input.grid(column=1, row=4, padx=20)
        
        self.inc_text = tk.Label(self, text="Incerteza")
        self.inc_text.grid(column=2, row=3)
        self.inc_input = tk.Entry(self, bd=5)
        self.inc_input.grid(column=2, row=4, padx=20)

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', 
                                      command=self.grab_value, font=("Courier", 16, 'bold'), fg='white', 
                                      relief='raised')
        self.calcular_btn.grid(column=1, row=40, pady=40)

app = Application()  
app.master.title('Prop incerteza')
app.mainloop()