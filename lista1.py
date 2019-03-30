from time import time
from decimal import Decimal
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Cria a tabela de index com o intervalo decidido
def cria_tabela_de_indexes(lista, intervalo):
    tabela_de_indexes = []

    for posicao in range(intervalo, len(lista), intervalo):
        tabela_de_indexes.append([posicao,lista[posicao]])
    return tabela_de_indexes


# Compara o alvo com os indices e retorna o indice mais "perto" do alvo
def procura_index(indices, alvo):
    auxiliarIndex = 0

    for i in indices:
        if alvo >= i[1]:
            auxiliarIndex = i[0]

    return auxiliarIndex

def busca_indexada(indices, lista, alvo):
    valorEncontrado = False
    index = procura_index(indices, alvo)

    for i in range(index,len(lista)):
        if lista[i] == alvo:
            return True

    if(valorEncontrado == False):
        return False

def busca_interpolada(lista, alvo):
    lo = 0
    hi = (len(lista) - 1)

    while lo <= hi and alvo >= lista[lo] and alvo <= lista[hi]:
        pos  = lo + int(((float(hi - lo) /
            ( lista[hi] - lista[lo])) * ( alvo - lista[lo])))

        if lista[pos] == alvo:
            return pos
        if lista[pos] < alvo:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1

def busca_sequencial(lista, alvo):
    i = 0
    # for i in range(len(lista)):
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return -1

def busca_sequencial_com_sentinela(lista, alvo):
    i = 0
    lista.append(alvo)
    while lista[i] != alvo:
        i += 1
    if i == (len(lista) -1):
        return -1
    return i

def busca_binaria(lista, alvo):
    primeiro = 0
    ultimo = len(lista) - 1
    i = 0

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        i += 1

        if lista[meio] == alvo:
            return meio
        else:
            if alvo < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    return -1

def plota_grafico(averages):
    plt.ylabel('Media de Tempo')

    for key in averages.keys():
        plt.bar(key, averages[key])

    plt.show()

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} wins)".format(pct, absolute)

def plota_grafico_pizza(wins):
    labels = wins.keys()
    valores = list(wins.values())
    ax = plt.subplots(figsize=(12, 9), subplot_kw=dict(aspect="equal"))[1]
    wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores), textprops=dict(color="w"))
    ax.legend(wedges, labels, title="Algoritimos", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Algoritimos de Busca")
    plt.show()

def calc_media(results):
    averages = {}

    for key in results.keys():
        averages[key] = sum(results[key]) / len(results[key])
    return averages

if __name__ == '__main__':
    results = {'Sequencial': [], 'Interpolada': [], 'Sentinela': [], 'Binaria': [], 'Indexada': []}
    result = {'Sequencial': 0, 'Interpolada': 0, 'Sentinela': 0, 'Binaria': 0, 'Indexada': 0}
    wins = {'Sequencial': 0, 'Interpolada': 0, 'Sentinela': 0, 'Binaria': 0, 'Indexada':0}

    for aux in range(1000):
        lista = [x for x in range(randint(1,1001))]
        numero_aleatorio = randint(1,len(lista))

        for key in result.keys():
            if key == 'Sequencial':
                inicio = time()
                busca_sequencial(lista, numero_aleatorio)
            elif key == 'Sentinela':
                inicio = time()
                busca_sequencial_com_sentinela(lista, numero_aleatorio)
            elif key == 'Binaria':
                inicio = time()
                busca_binaria(lista, numero_aleatorio)
            elif key == 'Indexada':
                index = cria_tabela_de_indexes(lista, 6)
                inicio = time()
                busca_indexada(index, lista, numero_aleatorio)
            else:
                inicio = time()
                busca_interpolada(lista, numero_aleatorio)

            fim = time()
            tempo = Decimal(fim - inicio)

            result[key] = tempo
            results[key].append(tempo)

        lis = list(result.items())
        winner = min(lis,key=lambda item:item[1])

        wins[winner[0]] += 1

    averages = calc_media(results)

    print('\n\t \t \tResultado em Wins:')
    for key in wins.keys():
        print(key + ': ' + str(wins[key]))

    print('\n\t \t \tMedia de Tempo:')
    for key in averages.keys():
        print(key + ': ' + str(averages[key]))

    plota_grafico_pizza(wins)
    plota_grafico(averages)
