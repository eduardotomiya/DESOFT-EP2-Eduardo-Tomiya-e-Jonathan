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

def afundados(dicionario_navios, tabuleiro):
    navios_afundados = 0
    for navios in dicionario_navios.values():
        posicoes = len(navios[0])
        for j in range(0, len(navios)):
            i = 0
            for e in range(0, len(navios[j])):
                linha = navios[j][e][0]
                coluna = navios[j][e][1]
                if tabuleiro[linha][coluna]== 'X':
                    i += 1
            if i == posicoes:
                navios_afundados += 1
    return navios_afundados

#Sexto Exercicio

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    lista_embarcacao_nova= define_posicoes(linha, coluna, orientacao, tamanho)
    for a in lista_embarcacao_nova:
        if a[0] > 9 or a[1] > 9:
                return False
    for inf in frota.values():
        q_de_embarcacoes=len(inf)
        for i in range(0, q_de_embarcacoes):
            lista_embarcacao=inf[i]
            for a in lista_embarcacao_nova:
                if a in lista_embarcacao:
                    return False
    return True

#Setimo Exercicio

