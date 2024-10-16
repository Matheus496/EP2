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
