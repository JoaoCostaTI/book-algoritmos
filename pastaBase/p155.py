grafo = {}

grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

infinito = float("inf")

custos = {"a": 6, "b": 2, "fim": infinito}

pais = {"a": "inicio", "b": "inicio", "fim": None}

processados = []

def ache_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        if custos[nodo] < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custos[nodo]
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_custo_mais_baixo(custos)

print(pais)