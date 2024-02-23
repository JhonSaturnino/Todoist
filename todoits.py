import tkinter as tk
import random

janela = tk.Tk()

janela.rowconfigure([0], weight=0) # redimensionameto automatico (linhas, weight = 1)
janela.columnconfigure([0, 1, 2], weight=1)

mensagem = tk.Label(text="Meutodoist", bg='black', fg='white', width='50', height='8')
mensagem.grid(row=0, column=0, columnspan=3, sticky="EW")
mensagem1 = tk.Label(text="Tarefas", bg='green', fg='white', width='50', height='5')
mensagem1.grid(row=1, column=0, sticky='new')
mensagem2 = tk.Label(text="Fazendo", bg='red', fg='white', width='50', height='5')
mensagem2.grid(row=1, column=1, sticky='ew')
mensagem3 = tk.Label(text="Feitas", bg='blue', fg='white', width='50', height='5')
mensagem3.grid(row=1, column=2, sticky='ew')

cores = ['blue', 'green', 'red', 'purple', 'yellow', 'pink', 'brown', 'orange']
linha = 4
posição = 0

def mudar_posição(botão):
    info = botão.grid_info()  # Obtem informações sobre a grade do botão
    if info:
        coluna_atual = info['column']
        if coluna_atual < 2:  # Verifica se está na coluna 0 ou 1
            botão.grid_forget()
            coluna_atual += 1
        else:
            coluna_atual = 0
        botão.grid(row=info['row'], column=coluna_atual)

def adicionar_tarefa(tarefa_texto=None):
    global linha, cores
    if tarefa_texto is None:  # Se nenhum texto for passado, obtém do campo de entrada
        tarefa_texto = tarefauserimput1.get()
        if not tarefa_texto:  # Se não houver texto, não faz nada
            return
    mensagem_tarefa = tk.Button(text=tarefa_texto, command=lambda: mudar_posição(mensagem_tarefa), bg=random.choice(cores), fg="black", width=40, height=2)
    mensagem_tarefa.grid(row=int(linha), column=0)
    linha += 1
    # Limpar o texto dos campos de entrada após adicionar a tarefa
    tarefauserimput1.delete(0, tk.END)
    
botão_adicionar = tk.Button(text="adicionar", command=adicionar_tarefa, bg="green", fg='white', width='10', height='2')
botão_adicionar.grid(row=3, column=0)
tarefauserimput1 = tk.Entry()
tarefauserimput1.grid(row=2, column=0, sticky="EW")
janela.mainloop()