dna = input()
base = input()
i = 0
seq = 0
maiorSeq = 0
posicao = 0
posicaoSeq = 0

if dna.count(base) == 0:
    print("ERRO")
else:
    while i < len(dna):
        if dna[i:i+1] == base:
            if dna[i-1:i] == base:
                seq = seq+1
            else:
                seq = 1
                posicao = i
        if seq > maiorSeq:
            maiorSeq = seq
            posicaoSeq = posicao
        i=i+1
    print(posicaoSeq)
    print(maiorSeq)