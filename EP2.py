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


frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicionario_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for embarcacao, qtde in dicionario_embarcacoes.items():
    
    for i in range(0, qtde[0]):
        print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if embarcacao != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

print(frota)

#Oitavo Exercicio

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

#------------------------ criando frota jogador ------------------------
frota_jogador = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicionario_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for embarcacao, qtde in dicionario_embarcacoes.items():
    
    for i in range(0, qtde[0]):
        print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if embarcacao != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])

tabuleiro_jogador = posiciona_frota(frota_jogador)
#------------------------------------------------------------------------------------------------

#----------------------------- criando frota oponente -----------------------------
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True

lista_ataques = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

    if linha_ataque not in range(0, 10):
        while linha_ataque not in range(0, 10):
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

    coluna_ataque = int(input('Coluna de ataque: '))

    if coluna_ataque not in range(0, 10):
        while coluna_ataque not in range(0, 10):
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual linha deseja atacar? '))

    ataque = [linha_ataque, coluna_ataque]

    if ataque in lista_ataques:
        while ataque in lista_ataques:
            print(f'A posição linha {ataque[0]} e coluna {ataque[1]} já foi informada anteriormente')

            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

            if linha_ataque not in range(0, 10):
                while linha_ataque not in range(0, 10):
                    print('Linha inválida!')
                    linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

            if coluna_ataque not in range(0, 10):
                while coluna_ataque not in range(0, 10):
                    print('Coluna inválida!')
                    coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

            ataque = [linha_ataque, coluna_ataque]

    else:
        lista_ataques.append(ataque)

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

        navios_afundados = afundados(frota_oponente, tabuleiro_oponente)

        if navios_afundados == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False

#Ultimo Exercicio
import random

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicionario_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for embarcacao, qtde in dicionario_embarcacoes.items():
    
    for i in range(0, qtde[0]):
        print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if embarcacao != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

print(frota)

navios_afundados = 0

tabuleiro = posiciona_frota(frota)

lista_oponente = []

linha_sorteada = random.randint(0, 9)
coluna_sorteada = random.randint(0, 9)

jogada = [linha_sorteada, coluna_sorteada]

if jogada in lista_oponente:
    while jogada in lista_oponente:
        linha_sorteada = random.randint(0, 9)
        coluna_sorteada = random.randint(0, 9)

        jogada = [linha_sorteada, coluna_sorteada]

else:
    print(f'Seu oponente está atacando na linha {linha_sorteada} e coluna {coluna_sorteada}')

tabuleiro = faz_jogada(tabuleiro, linha_sorteada, coluna_sorteada)

navios_afundados = afundados(frota, tabuleiro)

if navios_afundados == 10:
    print('Xi! O oponente derrubou toda a sua frota =(')