import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

def baixar_pdf(url, nome_arquivo):
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        with open(nome_arquivo, 'wb') as arquivo:
            for chunk in resposta.iter_content(1024):
                arquivo.write(chunk)
        print(f"Download concluído: {nome_arquivo}")
    else:
        print(f"Erro ao baixar {url}")

def main():
    url_site = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    resposta = requests.get(url_site)
    
    if resposta.status_code != 200:
        print("Erro ao acessar o site.")
        return
    
    soup = BeautifulSoup(resposta.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    pdf_links = [link['href'] for link in links if link['href'].endswith('.pdf') and ('anexo-i' in link['href'].lower() or 'anexo-ii' in link['href'].lower())]
    
    if not pdf_links:
        print("Nenhum PDF encontrado.")
        return
    
    os.makedirs("downloads", exist_ok=True)
    arquivos_baixados = []
    
    for pdf_link in pdf_links:
        nome_arquivo = os.path.join("downloads", pdf_link.split('/')[-1])
        baixar_pdf(pdf_link, nome_arquivo)
        arquivos_baixados.append(nome_arquivo)
    
    zip_filename = "anexos.zip"
    with ZipFile(zip_filename, 'w') as zipf:
        for arquivo in arquivos_baixados:
            zipf.write(arquivo, os.path.basename(arquivo))
    
    print(f"Arquivos compactados em: {zip_filename}")

if __name__ == "__main__":
    main()
