from funcoes import posicao_valida
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import posiciona_frota
from funcoes import monta_tabuleiros
from funcoes import faz_jogada
from funcoes import afundados
import random as rn

rn.seed(2)
navios =['porta-aviões','navio-tanque','navio-tanque','contratorpedeiro','contratorpedeiro','contratorpedeiro','submarino','submarino','submarino','submarino']
tamanhos = {'porta-aviões': 4,'navio-tanque':3,'contratorpedeiro':2,'submarino':1}
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
linha = 11
coluna = 11
orient = 11     
for navio in navios:
    tamanho = tamanhos[navio]
    while posicao_valida(frota,linha,coluna,orient,tamanho)==False:
        
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if navio != 'submarino':
            orient = int(input('[1] Vertical [2] Horizontal >'))
            if orient == 1:
                orient = 'vertical'
            else:
                orient = 'horizontal'
        if posicao_valida(frota,linha,coluna,orient,tamanho)==False:
            print('Esta posição não está válida!')
    
    frota = preenche_frota(frota,navio,linha,coluna,orient,tamanho)


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
tabubuleiro_jog = posiciona_frota(frota)

jogando = True

while jogando == True:
    tabuleiro_oponente = posiciona_frota(frota_oponente)
    tabubuleiro_jog = posiciona_frota(frota)
    posicao = []
    ataques_op = []
    tabuleiros = monta_tabuleiros(tabubuleiro_jog,tabuleiro_oponente)
    print(tabuleiros)
    while True:

        linha_ata = int(input('Jogador, qual linha deseja atacar?'))
    
        while  linha_ata > 9 or linha_ata< 0 :
            print('Linha inválida!')
            linha_ata = int(input('Jogador, qual linha deseja atacar?'))
    
        coluna_ata = int(input('Jogador, qual coluna deseja atacar?'))
        
        while coluna_ata > 9 or coluna_ata < 0 :
            print('Coluna inválida!')
            coluna_ata = int(input('Jogador, qual coluna deseja atacar?'))
        
        if [linha_ata,coluna_ata] in posicao:
            print(f'A posição linha {linha_ata} e coluna {coluna_ata} já foi informada anteriormente!')
            continue
        
        posicao.append([linha_ata,coluna_ata])

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linha_ata,coluna_ata)
        n_afund = afundados(frota_oponente,tabuleiro_oponente)
        
        if n_afund == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
            break
        
        
        oponente_linha_ata = rn.randint(0,9)
        oponente_col_ata = rn.randint(0,9)
        
        while [oponente_linha_ata,oponente_col_ata] in ataques_op:
            oponente_linha_ata = rn.randint(0,9)
            oponente_col_ata = rn.randint(0,9)
        ataques_op.append([oponente_linha_ata,oponente_col_ata])
        print(f'Seu oponente está atacando na linha {oponente_linha_ata} e coluna {oponente_col_ata}')
        
        tabubuleiro_jog = faz_jogada(tabubuleiro_jog,oponente_linha_ata,oponente_col_ata)
        n_afund_jog = afundados(frota,tabubuleiro_jog)

        if n_afund_jog == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
            break
        
        tabuleiros = monta_tabuleiros(tabubuleiro_jog,tabuleiro_oponente)
        print(tabuleiros)
        