from collections import deque

grafo = {
    "voce": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob":["anuj", "peggy"],
    "claire":["thom", "jonny"],
    "peggy": [],
    "anuj": [],
    "thom": [],
    "jonny": []
}

#Criação da lista
#fila_de_pesquisa = deque()

#adicionar todos os seus vizinhos para a lista de pesquisa
#fila_de_pesquisa += grafo["voce"]

#Função se a pessoa é vendedor

def pessoa_e_vendedor(nome):
    return nome[-1] == "m"


##################################
def pesquisa (nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print (pessoa + " é um vendedor de manga! ")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

pesquisa("voce")
