import tkinter as tk
from tkinter import ttk
import re
from database.db_manager import salvar_dados

def abrir_janela_cadastro():
    janela = tk.Toplevel()
    janela.title("PDV - Cadastro de Clientes")
    janela.geometry("980x600")
    janela.attributes("-topmost", True)

    frame = tk.Frame(janela)
    frame.place(rely=0, relx=0, relwidth=1, relheight=1)  # expand True para centralizar no meio

    # Funções de validação e formatação
    def validar_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def validar_telefone(telefone):
        return re.match(r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$", telefone) is not None

    def cadastrar_cliente():
        nome = entrada_nome.get().strip()
        email = entrada_email.get().strip()
        telefone = entrada_telefone.get().strip()
        endereco = entrada_endereco.get().strip()

        if not nome:
            aviso["text"] = "Nome não pode estar vazio!"
            return
        if not validar_telefone(telefone):
            aviso["text"] = "Telefone inválido!"
            return
        if not endereco:
            aviso["text"] = "Endereço não pode estar vazio!"
            return

        # Formatar telefone (Exemplo: "(XX) XXXX-XXXX")
        telefone = re.sub(r"[^\d]", "", telefone)
        telefone = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"

        salvar_dados(nome, email, telefone, endereco)  # Chamando a função de salvamento corretamente

    #criando o formulario de cadastro de clientes
    ttk.Label(frame, text="Preencha o formulário para cadastrar o cliente!", font=("Comic Sans MS", 20)).place(relx=0.5, rely=0.05, anchor="center")

    ttk.Label(frame, text="Nome:", font=("Comic Sans MS", 14)).place(relx=0.25, y=150, anchor="w")
    entrada_nome = ttk.Entry(frame)
    entrada_nome.place(width=500, height=25, relx=0.25, y=170, anchor='w')

    ttk.Label(frame, text="E-mail:", font=("Comic Sans MS", 14)).place(relx=0.25, y=220, anchor="w")
    entrada_email = ttk.Entry(frame)
    entrada_email.place(width=500, height=25, relx=0.25, y=240, anchor="w")

    ttk.Label(frame, text="Telefone:", font=("Comic Sans MS", 14)).place(relx=0.25, y=290, anchor="w")
    entrada_telefone = ttk.Entry(frame)
    entrada_telefone.place(width=500, height=25, relx=0.25, y=310, anchor="w")

    ttk.Label(frame, text="Endereço:", font=("Comic Sans MS", 14)).place(relx=0.25, y=360, anchor="w")
    entrada_endereco = ttk.Entry(frame)
    entrada_endereco.place(width=500, height=25, relx=0.25, y=380, anchor="w")

    #Botão de submissão
    botao_cadastro = tk.Button(frame, text="CADASTRAR", command=cadastrar_cliente, font=("Arial", 14), bg="#007bff", fg="white")
    botao_cadastro.place(width=170, height=50, relx=0.5, y=450, anchor="center")

    # Avisos
    aviso = ttk.Label(frame, text="", foreground="red")
    aviso.place(relx=0.5, y=520, anchor="center")

    # Execução da janela
    janela.mainloop()
