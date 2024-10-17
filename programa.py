from funcoes import posicao_valida
from funcoes import define_posicoes
from funcoes import preenche_frota



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

print(frota)