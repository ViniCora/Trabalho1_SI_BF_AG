# Algoritmo Genetico para o problema da Mochila feito pelos alunos Vinicius Coradassi e Arlei


from random import getrandbits

def itens_na_mochila(tamanho):
    return [ getrandbits(1) for x in range(tamanho) ]

def popula(itens_mochila, n_cromossomos):
    populacao = []
    for n in range(n_cromossomos):
        populacao.append(itens_na_mochila(len(itens_mochila)))

    print(populacao)

    return populacao

def avalia():
    return

def seleciona():
    return

def cruzamento():
    return

def mutacao():
    return

def calcula_fitness():
    return

def inicia_AG(n_geracoes, itens_mochila, n_cromossomos):

    populacao = popula(itens_mochila, n_cromossomos)
    print(len(itens_mochila))
 ##   for x in range(n_geracoes):
 ##       for i in itens_mochila:
 ##           print(i["valor"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    W = 100
    n_geracoes = 50
    n_cromossomos = 50
    itens_mochila = [
    {"valor": 50, "peso": 30},
    {"valor": 70, "peso": 20},
    {"valor": 40, "peso": 15},
    {"valor": 90, "peso": 10},
    {"valor": 60, "peso": 25},
    {"valor": 20, "peso": 5},
    {"valor": 85, "peso": 40},
    {"valor": 30, "peso": 12},
    {"valor": 55, "peso": 18},
    {"valor": 75, "peso": 8}]

    inicia_AG(n_geracoes, itens_mochila, n_cromossomos)

