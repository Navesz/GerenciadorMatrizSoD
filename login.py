import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from projeto import inicializar_janela_principal

def validar_login(usuario, senha):
    if usuario == "admin" and senha == "admin":
        return True
    return False

def tela_login():
    def verificar_credenciais():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if validar_login(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            janela_login.destroy()
            inicializar_janela_principal()
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos!")

    janela_login = tk.Toplevel()
    janela_login.title("Login")
    janela_login.geometry("300x150")

    label_usuario = tk.Label(janela_login, text="Usuário:")
    label_usuario.grid(row=0, column=0, padx=10, pady=10)

    entry_usuario = tk.Entry(janela_login)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    label_senha = tk.Label(janela_login, text="Senha:")
    label_senha.grid(row=1, column=0, padx=10, pady=10)

    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=10)

    botao_login = tk.Button(janela_login, text="Entrar", command=verificar_credenciais)
    botao_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

janela = tk.Tk()
janela.withdraw()

tela_login()
janela.mainloop()