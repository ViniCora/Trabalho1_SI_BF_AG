from random import getrandbits, random, randint
import numpy as np
import copy
import math
def sorteia_item_inicial(itens_mochila, peso_maximo):
  individuo = []
  valor = 0
  peso = 0
  for c in itens_mochila:
    bit = getrandbits(1)
    individuo.append(bit)
    if bit == 1:
      valor += c['valor']
      peso += c['peso']

  if peso > peso_maximo:
    valor = 0

  return {
    'individuo': individuo,
    'valor': valor,
    'peso': peso
  }

def organiza_peso_valores(itens_pesquisa):
  return sorted(itens_pesquisa, key=lambda item: (item['valor']), reverse=True)

def reavalia_valores_pesos(novo_item, itens_mochila, peso_max):
  novo_item['valor'] = 0
  novo_item['peso'] = 0
  for i in range(len(itens_mochila)):
    if novo_item['individuo'][i] == 1:
      novo_item['valor'] += itens_mochila[i]['valor']
      novo_item['peso'] += itens_mochila[i]['peso']

  if novo_item['peso'] > peso_max:
    novo_item['valor'] = 0

  return novo_item

def seleciona_vizinho(item, itens_mochila, peso_max):
    i = randint(0, len(item) - 1)
    novo_item = copy.deepcopy(item)
    if novo_item['individuo'][i] == 0:
      novo_item['individuo'][i] = 1
    else:
      novo_item['individuo'][i] = 0

    novo_item['individuo_pai'] = item['individuo']

    return reavalia_valores_pesos(novo_item, itens_mochila, peso_max)

def tempera_simulada(itens_pesquisa, itens_mochila, peso_max, k):
  temperatura = randint(500, 5000)
  multiplicador_temperatura = 0.98
  solucoes_atuais = []
  print("Itens Iniciais: ", itens_pesquisa)
  while temperatura > 0.05:
    solucoes_atuais.clear()
    for item in itens_pesquisa:
      for repeticoes in range(k):
          item_selecionado = seleciona_vizinho(item, itens_mochila, peso_max)
          delta = item_selecionado['valor'] - item['valor']
          if delta > 0:
            solucoes_atuais.append(item_selecionado)
          else:
            delta_porcentagem = delta / temperatura
            #print("Delta Porcentagem: ", delta_porcentagem)
            porcentagem_aceitar = (math.e ** delta_porcentagem)
            #print("Porcentagem Aceitar: ", porcentagem_aceitar)
            porcentagem_randomica = random()
            #print("Porcentagem Random: ", porcentagem_randomica)
            if porcentagem_randomica < porcentagem_aceitar:
              solucoes_atuais.append(item_selecionado)
    itens_totais = itens_pesquisa + solucoes_atuais
    itens_totais = organiza_peso_valores(itens_totais)
    itens_pesquisa = itens_totais[:k]
    temperatura *= multiplicador_temperatura

  return itens_pesquisa

def inicia_busca_em_feixe(quantidade_feixes, itens_mochila, peso_max):
  itens_pesquisa = []
  for n in range(quantidade_feixes):
    itens_pesquisa.append(sorteia_item_inicial(itens_mochila, peso_max))

  melhores_solucoes = tempera_simulada(itens_pesquisa, itens_mochila, peso_max, quantidade_feixes)
  print("Melhores Soluções:")
  print(melhores_solucoes)

def main():
  quantidade_feixes = randint(10, 100)
  peso_max = 100
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

  inicia_busca_em_feixe(quantidade_feixes, itens_mochila, peso_max)

if __name__ == "__main__":
  main()