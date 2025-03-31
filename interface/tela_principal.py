import tkinter as tk
from tkinter import ttk
from models.clientes import abrir_janela_cadastro
from datetime import datetime

# Obtém a data e hora atuais
data_e_hora = datetime.now()
# Formata a data e hora
data_formatada = data_e_hora.strftime("%d/%m/%Y")  # Exemplo: "23/03/2025"
hora_formatada = data_e_hora.strftime("%H:%M:%S")  # Exemplo: "08:15:00"
versao = "1.0.0"
usuario = "Feito Perfeito"

    
def iniciar_tela_principal():
    janela = tk.Tk()
    janela.title("PDV")
    janela.geometry("1280x720")
    janela.configure(bg="lightblue")


    # Criar um contêiner (Frame)
    frame = tk.Frame(janela, width=1280, height=620, bg="lightblue")
    frame.place(rely=0.1, relx=0, relwidth=1, relheight=1)  # expand True para centralizar no meio

    estilo = ttk.Style()
    estilo.configure("My.TLabel", background="lightblue", foreground="black")  # Define a cor de fundo
    estilo.configure("label.TLabel", background="#000", foreground="white")  # Define a cor de fundo

    ttk.Label(janela, text="OLÁ FEITO PERFEITO, TENHA UM BOM DIA!", style="My.TLabel", font=("DM Sans", 20)).place(relx=0.5, rely=0.05, anchor="center")

    botao_cadastro_produto = tk.Button(frame, text="CADASTRAR PRODUTO", command="", bg="#000", fg="white", font=("Arial", 14))
    botao_cadastro_produto.place(width=300, height=100, relx=0.1, rely=0.2)

    botao_cadastro_cliente = tk.Button(frame, text="CADASTRAR CLIENTE", command=abrir_janela_cadastro, bg="#000", fg="white", font=("Arial", 14))
    botao_cadastro_cliente.place(width=300, height=100, relx=0.4, rely=0.2)

    botao_relatorio = tk.Button(frame, text="RELATORIO", command="", bg="#000", fg="white", font=("Arial", 14))
    botao_relatorio.place(width=300, height=100, relx=0.7, rely=0.2)

    botao_vendas = tk.Button(frame, text="VENDAS", command="", bg="#000", fg="white", font=("Arial", 14))
    botao_vendas.place(width=300, height=100, relx=0.1, rely=0.4)

    botao_pdv = tk.Button(frame, text="PDV", command='', bg="#000", fg="white", font=("Arial", 14))
    botao_pdv.place(width=300, height=100, relx=0.4, rely=0.4)

    botao_balanceamento = tk.Button(frame, text="BALANCEAMENTO", command="", bg="#000", fg="white", font=("Arial", 14))
    botao_balanceamento.place(width=300, height=100, relx=0.7, rely=0.4)

    frame_footer = tk.Frame(frame, width=1280, height=100, bg="#000")
    frame_footer.place(rely=0.84, relx=0, relwidth=1, relheight=1)  # expand True para centralizar no meio

    ttk.Label(frame_footer, text="DATA: " + data_formatada, style="label.TLabel", font=("Arial", 12)).place(relx=0.10, rely=0.016)
    ttk.Label(frame_footer, text="HORA: " + hora_formatada, style="label.TLabel", font=("Arial", 12)).place(relx=0.30, rely=0.016)
    ttk.Label(frame_footer, text="VERSÃO: " + versao, style="label.TLabel", font=("Arial", 12)).place(relx=0.50, rely=0.016)
    ttk.Label(frame_footer, text="USUARIO: " + usuario, style="label.TLabel", font=("Arial", 12)).place(relx=0.70, rely=0.016)
    
    janela.mainloop()