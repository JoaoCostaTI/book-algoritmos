def sauda2 (nome):
    print("Como vai " + nome + "?")

def tchau(nome):
    print("Tchau " + nome + " <3")

def sauda (nome):
    print("Olá," + nome + "!")
    sauda2 (nome)
    print("Preparando para dizer tchau")
    tchau(nome)
sauda ("João")