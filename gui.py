import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def test(self):
        print('Estou calculando...')

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

        self.calcular_btn = tk.Button(self, text="Calcular", background='blue', justify=tk.CENTER, command=self.test)
        self.calcular_btn.grid()

app = Application()                     
app.master.title('Sample application')
app.mainloop()