import tkinter as tk
from tkinter import font, messagebox
from time import sleep

var_list = list()
val_list = list()
inc_list = list()

svar_list = list()
sval_list = list()
sinc_list = list()

def calcular(equation, latex, **kwargs):
    # Pegando a equação. Só existe uma equação
    print('Equação: ', equation)
    # Variáveis(var), valores(val) e incertezas(inc)
    print("Variáveis, valores e incertezas: ", kwargs)
    # Símbolo do latex
    print("Latex: ", latex)

    # REALIZE O CÁLCULO AQUI, CÉSAR!!!!!!!!!
    '''
    - EQUAÇÃO -> equation
    - Latex -> latex

    - VALORES -> val_list
    - VARIÁVEIS -> var_list
    - INCERTEZAS -> inc_list
    '''
















    # FIM

    # Retorna o resultado
    result = 'Aqui você envia o resultado do cálculo, japoneix'
    latex_result = 'Aqui você envia o resultado do latex, japoneix'

    if latex_result == None or latex_result == '' or latex_result == ' ':
        latex_result = "Você não providenciou o latex!"

    # Finaliza o processo
    window.destroy()

    # Abre a janela de resultado
    res_window = tk.Tk()
    res_window.resizable(False, False)
    result_window = ResultWindow(master=res_window, result=result, latex=latex_result, equacao=equation, valores=val_list, variaveis=var_list, incertezas=inc_list)
    result_window.master.title('Resultado')
    result_window.mainloop()

class ResultWindow(tk.Frame):
    result = str
    latex = str
    equacao = str
    
    # Conjuntos
    variaveis = list
    valores = list
    incertezas = list

    def __init__(self, master=None, result=result, latex=latex, equacao=equacao, variaveis=variaveis, valores=valores, incertezas=incertezas):
        self.result = result
        self.latex = latex
        self.equacao = equacao

        # Conjuntos
        self.variaveis = variaveis
        self.valores = valores
        self.incertezas = incertezas

        tk.Frame.__init__(self, master, background='grey') 
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.titulo_result = tk.Label(self, foreground='white', background='grey', text="Resultado", font=('Courier', 15, 'bold'))
        self.titulo_result.grid(column=1, row=0, pady=30)

        self.show_result = tk.Label(self, text=str(self.result), 
                                    background='cyan', padx=20, pady=20)
        self.show_result.grid(column=1, row=1)

        self.titulo_latex = tk.Label(self, foreground='white', background='grey', text="Latex", font=('Courier', 15, 'bold'))
        self.titulo_latex.grid(column=1, row=2, pady=30)

        self.show_latex = tk.Label(self, text=str(self.latex), 
                                    background='orange', padx=20, pady=20)
        self.show_latex.grid(column=1, row=3)

        self.titulo_dados = tk.Label(self, foreground='white', background='grey', text="Dados inseridos", font=('Courier', 15, 'bold')).grid(column=1, row=4, pady=30)

        msg = f"Equação: {self.equacao}.\n\nLatex: {self.latex}.\n\nValores: {self.valores}.\n\nVariáveis {self.variaveis}.\n\nIncertezas {self.incertezas}"
        
        self.show_dados = tk.Label(self, text=msg, background='black', foreground='white')
        self.show_dados.grid(column=1, row=5)

count = 5

window = tk.Tk()
window.resizable(False, False)
# window.geometry('400x500')

class Application(tk.Frame):

    def __init__(self, master=window):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        # Tem de chamar esse método pra funcionar o width e o height do Frame
        # self.grid_propagate(False)

    def main(self):

        if self.eq_input.get() == None or self.eq_input.get() == '' or self.eq_input.get() == ' ':
            messagebox.showerror('Erro', 'Sua equação está incompleta!')

        elif self.val_input == None or self.val_input.get() == '' or self.val_input.get() == ' ' or  self.var_input == None or self.var_input.get() == '' or self.var_input.get() == ' ' or  self.inc_input == None or self.inc_input.get() == '' or self.inc_input.get() == ' ' :
            messagebox.showerror('Erro', "Dados inválidos, verifique os campos de 'Variáveis', 'Valores' e 'Incertezas'!")
        
        else:
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
                latex=self.latex.get(),
                var=var_list, 
                val=val_list,
                inc=inc_list,
                )

    # Tutorial do spray
    def show_info_box(self):
        messagebox.showinfo('Como calcular?', "1 - Inserir a equação na caixa de 'Equação'\n2 - Inserir as 'Variáveis', 'Valores' e 'Incertezas' em suas respectivas caixas\n3 - Para adicionar mais campos de 'Variáveis', 'Valores' e 'Incertezas', aperte o botão '+' (verde)\n4 - Opcionalmente, adicione o símbolo do latex na caixa 'latex'\n5 - Aperte o botão 'Calcular' (azul)")

    def create_input(self):
        global count
        count += 1
         
        self.var1 = tk.Entry(self, bd=5, cursor='pencil')
        self.var1.grid(column=0, row=count, padx=20)

        self.val1 = tk.Entry(self,bd=5, cursor='pencil')
        self.val1.grid(column=1, row=count)

        self.inc1 = tk.Entry(self,bd=5, cursor='pencil')
        self.inc1.grid(column=2, row=count)

        svar_list.append(self.var1)
        sval_list.append(self.val1)
        sinc_list.append(self.inc1)

    def delete_input(self):

        if len(sval_list) > 0:
            # Destrói os objetos
            svar_list[-1].destroy()
            sval_list[-1].destroy()
            sinc_list[-1].destroy()

            # Diminui o tamanho das listas
            svar_list.pop(-1)
            sval_list.pop(-1)
            sinc_list.pop(-1)

    def createWidgets(self):

        self.titulo = tk.Label(self, text="Prop incerteza", font=('Courier', 15, 'bold'))
        self.titulo.grid(column=1, row=0, pady=30)

        self.info_icon = tk.Button(
            self, text="?", 
            command=self.show_info_box, fg='black', 
            relief='flat', font=('Helvetica', 12, 'bold', 'underline'), cursor='x_cursor'
        ).grid(column=2, row=0)

        self.latex_titulo = tk.Label(self, text="Latex", font=('Courier', 12)).grid(column=2, row=1)
        self.latex = tk.Entry(self, bd=5, cursor='pencil')
        self.latex.grid(column=2, row=2)

        self.eq_text = tk.Label(self, text="Equação", font=('Courier', 12)).grid(column=1, row=1)
        self.eq_input = tk.Entry(self, bd=5, cursor='pencil')
        self.eq_input.grid(column=1, row=2)

        self.add_input_btn = tk.Button(self, text="+", background='green', 
                                      command=self.create_input, fg='white', 
                                      relief='flat', padx=5, cursor='x_cursor')
        self.add_input_btn.grid(column=0, row=39)

        self.del_input_btn = tk.Button(self,  text="-", background='red', 
                                       command=self.delete_input, fg='black', 
                                      relief='flat', padx=5, cursor='x_cursor')
        self.del_input_btn.grid(column=2, row=39)

        self.var_text = tk.Label(self, text="Variável")
        self.var_text.grid(column=0, row=3)
        self.var_input = tk.Entry(self, bd=5, cursor='pencil')
        self.var_input.grid(column=0, row=4, padx=20)

        self.val_text = tk.Label(self, text="Valor")
        self.val_text.grid(column=1, row=3)
        self.val_input = tk.Entry(self, bd=5, cursor='pencil')
        self.val_input.grid(column=1, row=4, padx=20)
        
        self.inc_text = tk.Label(self, text="Incerteza")
        self.inc_text.grid(column=2, row=3)
        self.inc_input = tk.Entry(self, bd=5, cursor='pencil')
        self.inc_input.grid(column=2, row=4, padx=20)

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', 
                                      command=self.main, font=("Courier", 16, 'bold'), fg='white', 
                                      relief='raised', cursor='x_cursor')
        self.calcular_btn.grid(column=1, row=40, pady=40)

app = Application()  
app.master.title('Prop incerteza')
app.mainloop()