#pip install pandas
#pip install matplotlib
#pip install openpyxl

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook

def cadastrar_sistema(codigo, nome):
    pass  # Implemente a lógica para cadastrar sistemas

def consultar_sistemas():
    pass  # Implemente a lógica para consultar sistemas

def cadastrar_perfil(codigo_sistema, nome_perfil, descricao):
    pass  # Implemente a lógica para cadastrar perfis de acesso

def consultar_perfis():
    pass  # Implemente a lógica para consultar perfis de acesso

def cadastrar_matriz_sod(codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2):
    pass  # Implemente a lógica para cadastrar matriz SoD

def consultar_matriz_sod():
    pass  # Implemente a lógica para consultar matriz SoD

def cadastrar_perfil_usuario(usuario, codigo_sistema, nome_perfil):
    pass  # Implemente a lógica para cadastrar perfil de usuário com crítica de conflito de interesse

def consultar_perfis_usuario(usuario):
    pass  # Implemente a lógica para consultar perfis associados aos usuários


def abrir_cadastro_perfis_usuario():
    janela_cadastro_perfis_usuario = tk.Toplevel()
    janela_cadastro_perfis_usuario.title('Cadastro de Perfis de Usuários')
    janela_cadastro_perfis_usuario.geometry('500x300')

    # Adicione aqui os campos e botões para cadastrar e consultar perfis de usuários

def abrir_cadastro_sistemas():
    janela_cadastro_sistemas = tk.Toplevel()
    janela_cadastro_sistemas.title('Cadastro de Sistemas')
    janela_cadastro_sistemas.geometry('500x300')

    # Adicione aqui os campos e botões para cadastrar sistemas


def abrir_cadastro_perfis():
    janela_cadastro_perfis = tk.Toplevel()
    janela_cadastro_perfis.title('Cadastro de Perfis de Acesso')
    janela_cadastro_perfis.geometry('500x300')

    # Adicione aqui os campos e botões para cadastrar perfis de acesso


def abrir_cadastro_matriz_sod():
    janela_cadastro_matriz_sod = tk.Toplevel()
    janela_cadastro_matriz_sod.title('Cadastro de Matriz SoD')
    janela_cadastro_matriz_sod.geometry('500x300')

    # Adicione aqui os campos e botões para cadastrar matriz SoD

def ler_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv"), ("Arquivos Excel", "*.xlsx")])
    if arquivo:
        if arquivo.endswith('.csv'):
            dados = pd.read_csv(arquivo)
        else:
            dados = pd.read_excel(arquivo)
        atualizar_tabela(dados)

def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])
    if arquivo:
        writer = pd.ExcelWriter(arquivo, engine='openpyxl')
        tabela_dados.to_excel(writer, index=False)
        writer.save()

def atualizar_tabela(dados):
    global tabela_dados
    tabela_dados = dados
    tabela.delete(*tabela.get_children())
    for index, row in dados.iterrows():
        tabela.insert('', 'end', values=row.tolist())

def gerar_grafico():
    pass

def autenticar_usuario():
    pass

# Criação da janela principal
def inicializar_janela_principal():
    janela = tk.Tk()
    janela.title('Gerenciamento da Matriz SoD')
    janela.geometry('800x600')

    botao_cadastro_perfis_usuario = ttk.Button(janela, text='Cadastrar Perfis de Usuários', command=abrir_cadastro_perfis_usuario)
    botao_cadastro_perfis_usuario.grid(row=0, column=6, padx=5, pady=5)

    botao_cadastro_sistemas = ttk.Button(janela, text='Cadastrar Sistemas', command=abrir_cadastro_sistemas)
    botao_cadastro_sistemas.grid(row=0, column=3, padx=5, pady=5)

    botao_cadastro_perfis = ttk.Button(janela, text='Cadastrar Perfis', command=abrir_cadastro_perfis)
    botao_cadastro_perfis.grid(row=0, column=4, padx=5, pady=5)

    botao_cadastro_matriz_sod = ttk.Button(janela, text='Cadastrar Matriz SoD', command=abrir_cadastro_matriz_sod)
    botao_cadastro_matriz_sod.grid(row=0, column=5, padx=5, pady=5)

    # Botões de ações
    botao_ler = ttk.Button(janela, text='Ler Arquivo', command=ler_arquivo)
    botao_ler.grid(row=0, column=0, padx=5, pady=5)

    botao_salvar = ttk.Button(janela, text='Salvar Arquivo', command=salvar_arquivo)
    botao_salvar.grid(row=0, column=1, padx=5, pady=5)

    botao_grafico = ttk.Button(janela, text='Gerar Gráfico', command=gerar_grafico)
    botao_grafico.grid(row=0, column=2, padx=5, pady=5)

    # Tabela de dados
    tabela = ttk.Treeview(janela, columns=('acesso', 'funcao'), show='headings')
    tabela.heading('acesso', text='Acesso')
    tabela.heading('funcao', text='Função')
    tabela.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    # Configurar colunas da janela
    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)
    janela.columnconfigure(2, weight=1)
    janela.columnconfigure(6, weight=1)

    # Configurar linhas da janela
    janela.rowconfigure(0, weight=0)
    janela.rowconfigure(1, weight=1)

    # Iniciar o loop da aplicação
    tabela_dados = pd.DataFrame()
    janela.mainloop()