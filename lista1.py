from time import time
from decimal import Decimal
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def busca_interpolada(lista, alvo): 
    # Procura os indices maximo e minimo 
    lo = 0
    hi = (len(lista) - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and alvo >= lista[lo] and alvo <= lista[hi]: 
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / 
            ( lista[hi] - lista[lo])) * ( alvo - lista[lo]))) 
  
        # Condition of target found 
        if lista[pos] == alvo: 
            return pos 
   
        # If x is larger, x is in upper part 
        if lista[pos] < alvo: 
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1; 
      
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

        #print(i, meio)
        i += 1

        if lista[meio] == alvo:
            return meio
        else:
            if alvo < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return -1

# pip3 install matplotlib
# pip3 install python3-tk
def plota_grafico(binaria, sequencial_com_sentinela, sequencial, interpolada, label):
    plt.ylabel(label)
    plt.bar('Interpolada', interpolada)
    plt.bar('Binaria', binaria)
    plt.bar('Sequencial com Sentinela', sequencial_com_sentinela)
    plt.bar('Sequencial', sequencial)
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

def define_media(lista):
    i = 0
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]
    return resultado / i

resultado_interpolada = []
resultado_binaria = []
resultado_sequencial = []
resultado_sequencial_sentinela = []
wins = {'Sequencial': 0, 'Interpolada': 0, 'Sequencial_Sentinela': 0, 'Binaria': 0}

for aux in range(1000):
    # Define uma lista já ordenada com tamanho aléatorio no intervalo (1,1001)
    lista = [x for x in range(randint(1,1001))]

    #Define um número aleatorio da lista a ser buscado
    numero_aleatorio = randint(1,len(lista))

    inicio = time()
    busca_interpolada(lista, numero_aleatorio)
    fim = time()

    interpolada = Decimal(fim - inicio)
    resultado_interpolada.append(interpolada)

    inicio = time()
    busca_binaria(lista, numero_aleatorio)
    fim = time()

    binaria = Decimal(fim - inicio)
    resultado_binaria.append(binaria)

    inicio = time()
    busca_sequencial(lista, numero_aleatorio)
    fim = time()

    sequencial = Decimal(fim - inicio)
    resultado_sequencial.append(sequencial)

    inicio = time()
    busca_sequencial_com_sentinela(lista, numero_aleatorio)
    fim = time()

    sequencial_com_sentinela = Decimal(fim - inicio)
    resultado_sequencial_sentinela.append(sequencial_com_sentinela)

    lis = [('Sequencial', sequencial), ('Sequencial_Sentinela', sequencial_com_sentinela), ('Binaria', binaria), ('Interpolada', interpolada)]
    winner = min(lis,key=lambda item:item[1])

    wins[winner[0]] += 1

print('\n\t \t \tResultado em Wins:')
print('Binaria:' + str(wins['Binaria']))
print('Sequencial:' + str(wins['Sequencial']))
print('Sequencial com sentinela:' + str(wins['Sequencial_Sentinela']))
print('Interpolada:' + str(wins['Interpolada']))
# print('Empate entre pelo menos dois algoritmos de busca: ' + str(aux - sum(wins.values())))

print('\n\t\tMédia de tempo\n')
print('Binaria: ' + str(define_media(resultado_binaria)))
print('Sequencial: ' + str(define_media(resultado_sequencial)))
print('Sequencial com sentinela: ' + str(define_media(resultado_sequencial_sentinela)))
print('Interpolada: ' + str(define_media(resultado_interpolada)))

plota_grafico_pizza(wins)
# plota_grafico(wins_binaria, wins_sequencial_sentinela, wins_sequencial, 'Wins')
plota_grafico(define_media(resultado_binaria), define_media(resultado_sequencial_sentinela), define_media(resultado_sequencial), define_media(resultado_interpolada), 'Média de Tempo')
