import tkinter as tk

janelaConta = tk.Tk()
janelaConta.title('Minha Calculadora')
janelaConta.geometry('800x600')

labelNum1 = tk.Label(janelaConta,text="Primeiro Número")
labelNum1.pack(padx=5,pady=5)
entryNum1 = tk.Entry(janelaConta)
entryNum1.pack(padx=5,pady=5)

labelNum2 = tk.Label(janelaConta,text="Segundo Número")
labelNum2.pack(padx=5,pady=5)
entryNum2 = tk.Entry(janelaConta)
entryNum2.pack(padx=5,pady=5)

janelaConta.mainloop()

