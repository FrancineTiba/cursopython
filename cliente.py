import tkinter # impotarta a biblioteca gráfica

janela = tkinter.Tk(fg='black') # criando janela com a função janela recebe tkinter
janela.title("Cadastro de Cliente") # Cria o titulo
janela.geometry("800x600") # Define as dimensões da janela

labelNomeCliente = tkinter.Label(janela, text="Nome do Cliente")
labelNomeCliente.pack(padx=5,pady=5) # O pack coloca um objeto em baixo do outro, o padx/y gera um espaço entre o outro.
entryNomeCliente = tkinter.Entry(janela, width=80) # Nome da variável, função  
entryNomeCliente.pack(padx=5,pady=5)


labelCpf = tkinter.Label(janela, text="CPF")
labelCpf.pack(padx=5,pady=5) # O pack coloca um objeto em baixo do outro, o padx/y gera um espaço entre o outro.
entryCpf = tkinter.Entry(janela, width=30) # Nome da variável que represente o nome do campo a ser preenchido, função  
entryCpf.pack(padx=5,pady=5)



labelEmail = tkinter.Label(janela, text="e-mail")
labelEmail.pack(padx=5,pady=5) # O pack coloca um objeto em baixo do outro, o padx/y gera um espaço entre o outro.
entryEmail = tkinter.Entry(janela, width=50) # Nome da variável que represente o nome do campo a ser preenchido, função  
entryEmail.pack(padx=5,pady=5)


labelDataNascimento = tkinter.Label(janela, text="Data de Nascimento")
labelDataNascimento.pack(padx=5,pady=5) # O pack coloca um objeto em baixo do outro, o padx/y gera um espaço entre o outro.
entryDataNascimento = tkinter.Entry(janela, width=30) # Nome da variável, função  
entryDataNascimento.pack(padx=5,pady=5)



labelCelular = tkinter.Label(janela, text="Celular")
labelCelular.pack(padx=5,pady=5) # O pack coloca um objeto em baixo do outro, o padx/y gera um espaço entre o outro.
entryCelular = tkinter.Entry(janela, width=30) # Nome da variável que represente o nome do campo a ser preenchido, função   
entryCelular.pack(padx=5,pady=5)


buttonGravar = tkinter.Button(janela, text="Gravar", width=10)
buttonGravar.pack(padx=5,pady=100)


janela.mainloop() # comando que manté o programa rodando tem que ser sempre o último comando da linha.










