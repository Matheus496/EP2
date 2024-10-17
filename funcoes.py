def define_posicoes(linha,coluna,orient,tamanho):
    i=0
    posicoes = []
   
    while i < tamanho:
        if orient == 'vertical':
            posicoes.append([linha+i,coluna])
        else:
            posicoes.append([linha,coluna+i])
        i+=1

    return posicoes
def preenche_frota(frota,navio,linha,coluna,orient,tamanho):
    if navio not in frota:
        frota[navio] = [define_posicoes(linha,coluna,orient,tamanho)]
    else:
        frota[navio].append(define_posicoes(linha,coluna,orient,tamanho))
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for navios in frota.values():
        for navio in navios:
            for pos in navio:
                tabuleiro[pos[0]][pos[1]] = 1
    return tabuleiro


def afundados(frota,tabuleiro):
    navios_afundados = 0
    for navios in frota.values():
        for navio in navios:
            ocupa = []

            for pos in navio:
                if tabuleiro[pos[0]][pos[1]] == 'X':
                    ocupa.append('X')
            if ocupa:
                if len(ocupa) == len(navio):
                    navios_afundados += 1
    return navios_afundados

def posicao_valida(frota,linha,coluna,orient,tamanho):
    escolha = define_posicoes(linha,coluna,orient,tamanho)
    for c in escolha:
        for num in c:
            if num > 9:
                return False
    for navios in frota.values():
        for navio in navios:
            for pos in navio:
                if pos in escolha:
                    return False
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
