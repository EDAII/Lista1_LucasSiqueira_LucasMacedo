from time import time
from decimal import Decimal
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

        print(i, meio)
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
def plota_grafico(sequencial, binaria, sequencial_com_sentinela):
    plt.ylabel('time')
    plt.bar("binaria", binaria)
    plt.bar("sequencial", sequencial)
    plt.bar("sequencial com sentinela",sequencial_com_sentinela)
    plt.show()

lista = [x for x in range(1, 1001)]

# print(lista)

inicio = time()
print("\n", busca_binaria(lista, 750))
fim = time()

binaria = Decimal(fim - inicio)
print(Decimal(fim - inicio))

inicio = time()
print("\n", busca_sequencial(lista, 750))
fim = time()

sequencial = Decimal(fim - inicio)
print(Decimal(fim - inicio))

inicio = time()
print("\n", busca_sequencial_com_sentinela(lista, 750))
fim = time()

sequencial_com_sentinela = Decimal(fim - inicio)

print(Decimal(fim - inicio))

plota_grafico(sequencial, binaria, sequencial_com_sentinela)
