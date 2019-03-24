from random import randint

n = int(input("Número de vezes para repetir o experimento:"))

#na posição 0, o número de viorias
#na posição 1, o número de perdas
trocou = [0, 0]
n_trocou = [0, 0]

for i in range(n):
    #colocamos o premio
    premio = randint(0,2)

    #escolhemos a porta
    escolhido = randint(0,2)

    #removemos uma porta (aleatória) vazia e que não tenhamos escolhido
    removido = randint(0,2)
    while removido == escolhido or removido == premio:
        removido = randint(0,3)

    #troca = 1, não troca = 0
    if randint(0,1):
        #decidimos para qual ele vai mudar
        #impedindo que ele mude para o que foi removido
        if removido == 0:
            if escolhido == 1:
                escolhido = 2
            else:
                escolhido = 1
        elif removido == 1:
            if escolhido == 0:
                escolhido = 2
            else:
                escolhido = 0
        else:
            if escolhido == 0:
                escolhido = 1
            else:
                escolhido = 0

        #verificamos se ele ganhou
        if escolhido == premio:
            trocou[0] += 1
        else:
            trocou[1] += 1

    #caso ele não tenha trocado de porta, verificamos se ele ganhou
    else:
        if escolhido == premio:
            n_trocou[0] += 1
        else:
            n_trocou[1] += 1

#impressão dos resultados
#(a ser trocado pelo plot dos gŕaficos)
print("Depois de repetir", n, "obtivemos:")
print("Trocando:")
print("---Ganhou:", trocou[0], "=", trocou[0] / n)
print("---Perdeu:", trocou[1], "=", trocou[1] / n)
print("Não Trocando:")
print("---Ganhou:", n_trocou[0], "=", n_trocou[0] / n)
print("---Perdeu:", n_trocou[1], "=", n_trocou[1] / n)
