import subprocess
import tkinter as tk
from tkinter import messagebox

def download_site(site, directory='BaixarSite'):
    if not site.startswith('http'):
        site = 'http://' + site
    command = f'wget --mirror --convert-links --adjust-extension --page-requisites --no-parent {site} -P {directory}'
    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Sucesso", f"Download completo! Site salvo em: {directory}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao baixar o site: {e}")

def on_download_button_click():
    site = url_entry.get()
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
