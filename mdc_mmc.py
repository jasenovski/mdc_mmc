import numpy as np

def divisor_comum(dimensoes, min_max = "max"):

    divisores = []
    for i in range(len(dimensoes)):
        divisores.append([])

    for i in range(len(divisores)):
        for j in range(1, min(dimensoes) + 1, 1):
            divisao = dimensoes[i] / j
            if int(divisao) == float(divisao):
                divisores[i].append(j)

    divisores_comuns = []
    for i in divisores[0]:
        verificacao = True
        for j in range(1, len(divisores), 1):
            if i not in divisores[j]:
                verificacao = False
                continue
        if verificacao == True:
            divisores_comuns.append(i)

    if min_max == "min":
        divisores_comuns.sort()
        if len(divisores_comuns) > 1:
            return divisores_comuns[1]
        else:
            return divisores_comuns[0]
    elif min_max == "max":
        return max(divisores_comuns)
    else:
        return divisores_comuns