import os
import wget
import tkinter as tk
from tkinter import messagebox

def download_site(site, directory='BaixarSite'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    try:
        file_name = wget.download(site, out=directory)
        messagebox.showinfo("Sucesso", f"Download completo! Arquivo salvo em: {file_name}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o site: {e}")

def on_download_button_click():
    site = url_entry.get()
    if not site.startswith('http'):
        site = 'http://' + site
    download_site(site)

# Criar a janela principal
root = tk.Tk()
root.title("Baixar Site")

# Adicionar um rótulo e uma entrada para o URL
tk.Label(root, text="URL do Site:").pack(padx=10, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=5)

# Adicionar um botão para iniciar o download
download_button = tk.Button(root, text="Baixar", command=on_download_button_click)
download_button.pack(padx=10, pady=20)

# Iniciar o loop principal da interface gráfica
root.mainloop()
