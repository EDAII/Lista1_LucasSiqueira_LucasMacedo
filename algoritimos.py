from time import time
from decimal import Decimal
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def busca_sequencial(lista, alvo):
    i = 0
    # for i in range(len(lista)):
    while i < len(lista):
        # print(i)
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
def plota_grafico(binaria, sequencial_com_sentinela, sequencial, label):
    plt.ylabel(label)
    plt.bar("binaria", binaria)
    plt.bar("sequencial com sentinela",sequencial_com_sentinela)
    plt.bar("sequencial", sequencial)
    plt.show()

def define_media(lista):
    i = 0
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]
    return resultado / i

resultado_binaria = []
resultado_sequencial = []
resultado_sequencial_sentinela = []
wins_binaria = 0
wins_sequencial = 0
wins_sequencial_sentinela = 0
aux = 0

while aux != 1000:
    # Define uma lista já ordenada com tamanho aléatorio no intervalo (1,1001)
    lista = [x for x in range(randint(1,1001))]

    #Define um número aleatorio da lista a ser buscado
    numero_aleatorio = randint(1,len(lista))

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

    if sequencial < binaria and sequencial < sequencial_com_sentinela:
        wins_sequencial += 1
    elif binaria < sequencial and binaria < sequencial_com_sentinela:
        wins_binaria += 1
    elif sequencial_com_sentinela < binaria and sequencial_com_sentinela < sequencial:
        wins_sequencial_sentinela += 1

    aux += 1

print("\n\t \t \tResultado em Wins: \n Binaria:" + str(wins_binaria) + '\n' ,"Sequencial:" + str(wins_sequencial) + '\n',"Sequencial com sentinela:" + str(wins_sequencial_sentinela) + '\n')
print("Empate entre pelo menos dois algoritmos de busca: " + str(aux - (wins_sequencial + wins_binaria + wins_sequencial_sentinela)))
print("\n\t\tMédia de tempo\n")
print("Binaria:" + str(define_media(resultado_binaria)), "\nSequencial:" + str(define_media(resultado_sequencial)),"\nSequencial com sentinela:" + str(define_media(resultado_sequencial_sentinela)))

plota_grafico(wins_binaria, wins_sequencial_sentinela, wins_sequencial, 'Wins')
plota_grafico(define_media(resultado_binaria), define_media(resultado_sequencial_sentinela), define_media(resultado_sequencial), 'Média de tempo')
