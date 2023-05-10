#Primeiro Exercicio

def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_p = []
    if orientacao == 'vertical':
        for espaco in range(tamanho):
            lista_p.append([linha+espaco, coluna])
    elif orientacao == 'horizontal':
        for espaco in range(tamanho):
            lista_p.append([linha, coluna+espaco])
    return lista_p

#Segundo Exercicio

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    lista = []
    if orientacao == 'vertical':
        for j in range(0, tamanho):
            lista.append([linha+j,coluna])
    if orientacao == 'horizontal':
        for e in range(0,tamanho):
            lista.append([linha, coluna+e])
    if nome in frota and lista != []:
        frota[nome] += [lista]
    if nome not in frota and lista != []:
        frota[nome] = [lista]
    return frota

#Terceiro Exercicio

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] ==1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

#Quarto Exercicio

def posiciona_frota(dicionario):
    retorno = []
    for i in range(0, 10):
        lista_2 = []
        for e in range(0, 10):
            lista_2.append(0)
        retorno.append(lista_2)
    for posicao in dicionario.values():
        for p in posicao:
            for espaco in p:
                retorno[espaco[0]][espaco[1]] = 1
    return retorno

#Quinto Exercicio 

