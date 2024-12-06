import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tkinter as tk
from tkinter import messagebox

def save_file(url, directory, session):
    response = session.get(url)
    parsed_url = urlparse(url)
    file_path = os.path.join(directory, parsed_url.path.lstrip('/'))
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(response.content)

def download_site(site, directory='BaixarSite'):
    session = requests.Session()
    response = session.get(site)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    base_url = "{0.scheme}://{0.netloc}".format(urlparse(site))
    os.makedirs(directory, exist_ok=True)

    # Baixar a página principal
    save_file(site, directory, session)
    
    # Baixar todos os arquivos CSS, JS e imagens
    tags = soup.find_all(['link', 'script', 'img'])
    for tag in tags:
        if tag.name == 'link' and 'stylesheet' in tag.get('rel', []):
            file_url = urljoin(base_url, tag['href'])
            save_file(file_url, directory, session)
        elif tag.name == 'script' and tag.get('src'):
            file_url = urljoin(base_url, tag['src'])
            save_file(file_url, directory, session)
        elif tag.name == 'img' and tag.get('src'):
            file_url = urljoin(base_url, tag['src'])
            save_file(file_url, directory, session)
    
    messagebox.showinfo("Sucesso", "Download completo!")

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
