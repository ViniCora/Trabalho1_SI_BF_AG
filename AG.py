# Algoritmo Genetico para o problema da Mochila feito pelos alunos Vinicius Coradassi e Arlei


from random import getrandbits, random, randint, choices
import time

def itens_na_mochila_fitness(itens_mochila):
    individuo = []
    valor = 0
    peso = 0
    for c in itens_mochila:
        bit = getrandbits(1)
        individuo.append(bit)
        if bit == 1:
            valor += c['valor']
            peso += c['peso']

    return {
        'individuo': individuo,
        'valor': valor,
        'peso': peso
    }

def organiza_peso_valores(populacao):
    return sorted(populacao, key=lambda item: (item['valor'], item['peso']), reverse=True)

def popula_calcula_fitness(itens_mochila, n_cromossomos):
    populacao = []
    for n in range(n_cromossomos):
        populacao.append(itens_na_mochila_fitness(itens_mochila))

    populacao = organiza_peso_valores(populacao)

    return populacao

def avalia():
    ##Função para avaliar parada do programa
    return

def seleciona(itens_mochila):
    ##roleta
    valor_total = sum(item['valor'] for item in itens_mochila)
    probabilidades = [item['valor'] / valor_total for item in itens_mochila]
    escolha = choices(itens_mochila, weights=probabilidades, k=1)
    item_escolhido = escolha[0]
    itens_mochila.remove(item_escolhido)
    return item_escolhido

def cruzamento(individuo1, individuo2):
    ##É passado dois individuos e faz o crossover
    valor_cross_over = randint(0, len(itens_mochila) - 1)
    novo_individuo = individuo1['individuo'][:valor_cross_over] + individuo2['individuo'][valor_cross_over:]
    mutacao(novo_individuo)

    return novo_individuo

def mutacao(novo_individuo):
    ##Selecionar uma posição e trocar seu valor (de 0 para 1 e de 1 para 0)
    if 0.05 > random():
        item = randint(0, len(novo_individuo) - 1)
        if (novo_individuo[item] == 1):
            novo_individuo[item] = 0
        else:
            novo_individuo[item] = 1

def calcula_novo_fitness(novo_individuo, itens_mochila):
    ##Usar para calcular a nova fitness após a retirada de um individuo -- talvez não precise pq a roleta se vira com os dados
    valor = 0
    peso = 0
    for n in range(len(novo_individuo)):
        if novo_individuo[n] == 1:
            valor += itens_mochila[n]['valor']
            peso += itens_mochila[n]['peso']

    return {
        'individuo': novo_individuo,
        'valor': valor,
        'peso': peso
    }

def evolucao(populacao, itens_mochila, n_cromossomos, n_geracoes, peso_maximo):

    ##Fazer uma copia para sempre ter remoção desse item
    iteracoes = n_cromossomos//2
    historico_melhores = []
    for i in range(n_geracoes):
        novos_individuos = []
        while len(novos_individuos) < n_cromossomos:
            itens_roleta = populacao.copy()
            individuo1 = seleciona(itens_roleta).copy()
            individuo2 = seleciona(itens_roleta).copy()
            novo_objeto = calcula_novo_fitness(cruzamento(individuo1, individuo2), itens_mochila)
            if(novo_objeto['peso'] <= peso_maximo):
                novos_individuos.append(novo_objeto)
        populacao= novos_individuos
        populacao = organiza_peso_valores(populacao)
        populacao = populacao[:n_cromossomos]
        novos_individuos.clear()

        historico_melhores.append(populacao[0])

    return populacao

def inicia_AG(n_geracoes, itens_mochila, n_cromossomos, peso_maximo):

    populacao = popula_calcula_fitness(itens_mochila, n_cromossomos)
    print("População inicial:", populacao)
    pop_final = evolucao(populacao, itens_mochila, n_cromossomos, n_geracoes, peso_maximo)
    print("Melhor Solução:", pop_final[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    W = 100
    n_geracoes = 100
    n_cromossomos = 20
    itens_mochila = [
    {'valor': 50, 'peso': 30},
    {'valor': 70, 'peso': 20},
    {'valor': 40, 'peso': 15},
    {'valor': 90, 'peso': 10},
    {'valor': 60, 'peso': 25},
    {'valor': 20, 'peso': 5},
    {'valor': 85, 'peso': 40},
    {'valor': 30, 'peso': 12},
    {'valor': 55, 'peso': 18},
    {'valor': 75, 'peso': 8}]

    inicio = time.time()
    inicia_AG(n_geracoes, itens_mochila, n_cromossomos, W)
    fim = time.time()
    print("Tempo de execução: ",fim - inicio)

