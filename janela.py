import tkinter as tk # importação da biblioteca
from tkinter import messagebox # è uma janela que aparece como resposta do processamento dos dados

def mostraFrase(): # def() ->  criou uma função para mostrar a frase
    nome =entryNome.get() #  get() -> Captura o nome para armazenar dentro da objeto(EntryNome) nome
    messagebox.showinfo("Saudações","Bom dia " + nome) # função que foi criada para exibir a mensagem no momento do clique no botão

janela = tk.Tk() #Função
janela.geometry('600x400') #Dimensões da area
janela.title('Curso Pyhon Senai') #Titulo

frase = tk.Label(janela, text='Meu primeiro programa grafico', bg='purple',fg='aqua', font=('Arial',26, )) #comando de saida, determinado pelo programador
frase.pack(padx=5,pady=10)

labelNome=tk.Label(janela,  text='Qual o seu nome?',fg = 'blue' ,font = ('Arial', 24) ) #comando de saida determinado pelo programdor
labelNome.pack(padx=5,pady=10)

entryNome = tk.Entry(janela) #comando de entrada que o usuário vai digitar o texto
entryNome.pack(padx=5,pady=10)

buttonFrase = tk.Button(janela, text='Clique-me',command = mostraFrase) # objeto de criação do botão
buttonFrase.pack(padx=5,pady=10)

janela.mainloop() # controla o tempo de permanência da janela aberta.