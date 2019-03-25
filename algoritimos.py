from time import time
from decimal import Decimal

def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        # print(i)
        if lista[i] == alvo:
            return i
    return -1

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

lista = [x for x in range(1, 1001)]

# print(lista)

inicio = time()
print("\n", busca_binaria(lista, 750))
fim = time()

print(Decimal(fim - inicio))

inicio = time()
print("\n", busca_sequencial(lista, 750))
fim = time()

print(Decimal(fim - inicio))