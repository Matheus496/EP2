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

