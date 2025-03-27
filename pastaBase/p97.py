caderno = dict()

caderno["maça"] = 0.67
caderno["leite"] =  1.49
caderno["abacate"] = 1.49
#print (caderno)

#print(caderno["abacate"])

lista_telefonica = {}

lista_telefonica["Joao Costa"] = 31992206233
lista_telefonica["Gustavo"] = 31720275
lista_telefonica["Alice"] = 14895452

#print (lista_telefonica["Joao Costa"])


#CONFERINDO SE UMA PESSOA JÁ ESTÁ NA LISTA DE VOTOS COMPUTADOS
votaram = {}

voted = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
       # print ("Mande Embora")
    #else:
        votaram[nome] = True
        #print("Deixe votar!")

verifica_eleitor("joao")
verifica_eleitor("alice")
verifica_eleitor("gustavo")
verifica_eleitor("alice")
verifica_eleitor("alice")

cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados
    
# Retorne 1 para qualquer entrada
