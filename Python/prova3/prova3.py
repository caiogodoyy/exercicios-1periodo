#ABRIR ARQUIVOS .TXT
xfile = open('corpus1.txt', "r", encoding="utf-8")
file = xfile.read()
xfile.close()
cfile = open('corpus usuario.txt', 'r')
file5 = cfile.read()
cfile.close()

#REMOVER PONTUAÇÃO
file = file.replace('–', '').replace('"', '').replace('.','').replace(',','').replace(';','').replace(':','').replace('?','').replace('-','').replace('(','').replace(')','').replace('/', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('º','').replace('%', '').replace('&', '').replace('#', '').replace('@', '').replace('!', '').replace('*', '').replace('#', '').replace('@', '').replace('!', '').replace('*', '').replace('ª', '').replace('—', '')
file5 = file5.replace('–', '').replace('"', '').replace('.','').replace(',','').replace(';','').replace(':','').replace('?','').replace('-','').replace('(','').replace(')','').replace('/', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('º','').replace('%', '').replace('&', '').replace('#', '').replace('@', '').replace('!', '').replace('*', '').replace('#', '').replace('@', '').replace('!', '').replace('*', '').replace('ª', '').replace('—', '')
#MINUSCULA
file = file.lower()
file5 = file5.lower()

#SEPARAÇÃO DE QUADRI/TRI/BI/UNIGRAMAS
palavras = file.split()
palavrasUser = file5.split()

#QUADRIGRAMA CORPUS PRINCIPAL
i = 0
quadrigramas = []
while i < len(palavras)-3:
    x = palavras[i] + " " + palavras[i+1] + " " + palavras[i+2] + " " + palavras[i+3]
    quadrigramas.append(x)
    i = i+1
#QUADRIGRAMA CORPUS USUARIO
i = 0
quadrigramasUser = []
while i < len(palavrasUser)-3:
    x = palavrasUser[i] + " " + palavrasUser[i+1] + " " + palavrasUser[i+2] + " " + palavrasUser[i+3]
    quadrigramasUser.append(x)
    i = i+1
#TRIDRIGRAMA CORPUS PRINCIPAL
i = 0
trigramas = []
while i < len(palavras)-2:
    x = palavras[i] + " " + palavras[i+1] + " " + palavras[i+2]
    trigramas.append(x)
    i = i+1
#TRIDRIGRAMA CORPUS USUARIO
i = 0
trigramasUser = []
while i < len(palavrasUser)-2:
    x = palavrasUser[i] + " " + palavrasUser[i+1] + " " + palavrasUser[i+2]
    trigramasUser.append(x)
    i = i+1
#BIGRAMA CORPUS PRINCIPAL
i = 0
bigramas = []
while i < len(palavras)-1:
    x = palavras[i] + " " + palavras[i+1]
    bigramas.append(x)
    i = i+1
#BIGRAMA CORPUS USUARIO
i = 0
bigramasUser = []
while i < len(palavrasUser)-1:
    x = palavrasUser[i] + " " + palavrasUser[i+1]
    bigramasUser.append(x)
    i = i+1
#ORDENAÇÃO UNIGRAMAS PRINCIPAL
counts1 = {}
for x in palavras:
    counts1[x] = counts1.get(x, 0) + 1
palavrasOrdenadas = {k: v for k, v in sorted(counts1.items(), key=lambda item: item[1], reverse=True)}
palavrasOrd = list(palavrasOrdenadas.keys())
#ORDENAÇÃO UNIGRAMAS USUARIO
counts1User = {}
for x in palavrasUser:
    counts1User[x] = counts1User.get(x, 0) + 1
palavrasOrdenadasUser = {k: v for k, v in sorted(counts1User.items(), key=lambda item: item[1], reverse=True)}
palavrasOrdUser = list(palavrasOrdenadasUser.keys())
#ORDENAÇÃO QUADRIGRAMAS PRINCIPAL
counts4 = {}
quadrigramasOrd = []
for x in quadrigramas:
    counts4[x] = counts4.get(x, 0) + 1
quadrigramasOrdenados = {k: v for k, v in sorted(counts4.items(), key=lambda item: item[1], reverse=True)}
for i in quadrigramasOrdenados:
    quadrigramasOrd.append(i)
#ORDENAÇÃO QUADRIGRAMAS USUARIO
counts4User = {}
quadrigramasOrdUser = []
for x in quadrigramasUser:
    counts4User[x] = counts4User.get(x, 0) + 1
quadrigramasOrdenadosUser = {k: v for k, v in sorted(counts4User.items(), key=lambda item: item[1], reverse=True)}
for i in quadrigramasOrdenadosUser:
    quadrigramasOrdUser.append(i)
#ORDENAÇÃO TRIGRAMAS PRINCIPAL
counts3 = {}
trigramasOrd = []
for x in trigramas:
    counts3[x] = counts3.get(x, 0) + 1
trigramasOrdenados = {k: v for k, v in sorted(counts3.items(), key=lambda item: item[1], reverse=True)}
for i in trigramasOrdenados:
    trigramasOrd.append(i)
#ORDENAÇÃO TRIGRAMAS USUARIO
counts3User = {}
trigramasOrdUser = []
for x in trigramasUser:
    counts3User[x] = counts3User.get(x, 0) + 1
trigramasOrdenadosUser = {k: v for k, v in sorted(counts3User.items(), key=lambda item: item[1], reverse=True)}
for i in trigramasOrdenadosUser:
    trigramasOrdUser.append(i)
#ORDENAÇÃO BIGRAMAS PRINCIPAL
counts2 = {}
bigramasOrd = []
for x in bigramas:
    counts2[x] = counts2.get(x, 0) + 1
bigramasOrdenados = {k: v for k, v in sorted(counts2.items(), key=lambda item: item[1], reverse=True)}
for i in bigramasOrdenados:
    bigramasOrd.append(i)
#ORDENAÇÃO BIGRAMAS USUARIO
counts2User = {}
bigramasOrdUser = []
for x in bigramasUser:
    counts2User[x] = counts2User.get(x, 0) + 1
bigramasOrdenadosUser = {k: v for k, v in sorted(counts2User.items(), key=lambda item: item[1], reverse=True)}
for i in bigramasOrdenadosUser:
    bigramasOrdUser.append(i)

textos_usuario = list()

sugestoes = []

def encerar_programa():
    exit()


def apagar_dados():
    print('A operação a seguir é irreversível!. Tem certeza que deseja apagar os dados do usuário? [S/N]')
    opcao = input('Opcação: ').upper()
    if opcao == 'S':
        file4 = open('corpus usuario.txt', 'w')
        file4.close()
        print('Dados apagados com sucesso!')


def escolher_dentre_sugestoes():
    print(f'Sugestões: [1] {sugestoes[0]} [2] {sugestoes[1]} [3] {sugestoes[2]} [4] {sugestoes[3]} [5] {sugestoes[4]} [I] Ignorar sugestões')
    sugestao_escolhida = input('Opção: ').upper()
    if sugestao_escolhida == 'I':
        return None
    else:
        indice = int(sugestao_escolhida) - 1
        return sugestoes[indice]



def iniciar_novo_texto():
    texto_corrente = ''
    paragrafo_corrente = ''
    print('\nEsse é o seu texto atual. Você deve digitar um parágrafo por vez.')
    print('A cada <ENTER> que você digitar, um menu irá aparecer com as seguintes opções:')
    print('[S] - Obter sugestões de palavras')
    print('[A] - Adicionar o parágrafo ao texto corrente e iniciar novo parágrafo')
    print('[D] - Descartar o parágrafo corrente e iniciar novo parágrafo')
    print('Continue a digitar o parágrafo após o texto corrente')

    while True:
        print('----------TEXTO CORRENTE----------')
        print(texto_corrente)
        paragrafo_corrente += input(paragrafo_corrente)
        print('O que você deseja fazer?')
        print('[S] - Obter sugestões de palavras')
        print('[A] - Adicionar o parágrafo ao texto corrente e iniciar novo parágrafo')
        print('[D] - Descartar o parágrafo corrente e iniciar novo parágrafo')
        opcao = input('Opção: ').upper()
        if opcao == 'S':
            sugestoes.clear()
            paragrafo_corrente2 = paragrafo_corrente
            paragrafo_corrente2 = paragrafo_corrente2.lower()
            teste = paragrafo_corrente2.split()
            #SUGESTAO USUARIO
            if len(teste) >= 3:
                ultimas_palavras = paragrafo_corrente2.split()
                ultimas_palavras = ultimas_palavras[-3] + " " + ultimas_palavras[-2] + " " + ultimas_palavras[-1]
                i = 0
                while len(quadrigramasOrdUser) > i:
                    espaco = quadrigramasOrdUser[i].rfind(" ")
                    if quadrigramasOrdUser[i][:espaco] == ultimas_palavras:
                        x = quadrigramasOrdUser[i].split()
                        if sugestoes.count(x[-1]) == 0:
                            sugestoes.append(x[-1])
                    i = i + 1
            #SUGESTAO PRINCIPAL
            if len(teste) >= 3:
                ultimas_palavras = paragrafo_corrente2.split()
                ultimas_palavras = ultimas_palavras[-3] + " " + ultimas_palavras[-2] + " " + ultimas_palavras[-1]
                i = 0
                while len(quadrigramasOrd) > i:
                    espaco = quadrigramasOrd[i].rfind(" ")
                    if quadrigramasOrd[i][:espaco] == ultimas_palavras:
                        x = quadrigramasOrd[i].split()
                        if sugestoes.count(x[-1]) == 0:
                            sugestoes.append(x[-1])
                    i = i + 1
            #SUGESTAO USUARIO
            if len(teste) >= 2:
                ultimas_palavras = paragrafo_corrente2.split()
                ultimas_palavras = ultimas_palavras[-2] + " " + ultimas_palavras[-1]
                i = 0
                while len(trigramasOrdUser) > i:
                    espaco = trigramasOrdUser[i].rfind(" ")
                    if trigramasOrdUser[i][:espaco] == ultimas_palavras:
                        x = trigramasOrdUser[i].split()
                        if sugestoes.count(x[-1]) == 0:
                            sugestoes.append(x[-1])
                    i = i + 1
            #SUGESTAO PRINCIPAL
            if len(teste) >= 2:
                ultimas_palavras = paragrafo_corrente2.split()
                ultimas_palavras = ultimas_palavras[-2] + " " + ultimas_palavras[-1]
                i = 0
                while len(trigramasOrd) > i:
                    espaco = trigramasOrd[i].rfind(" ")
                    if trigramasOrd[i][:espaco] == ultimas_palavras:
                        x = trigramasOrd[i].split()
                        if sugestoes.count(x[-1]) == 0:
                            sugestoes.append(x[-1])
                    i = i + 1
            #SUGESTAO USUARIO
            ultimas_palavras = paragrafo_corrente2.split()
            ultimas_palavras = ultimas_palavras[-1]
            i = 0
            while len(bigramasOrdUser) > i:
                espaco = bigramasOrdUser[i].rfind(" ")
                if bigramasOrdUser[i][:espaco] == ultimas_palavras:
                    x = bigramasOrdUser[i].split()
                    if sugestoes.count(x[-1]) == 0:
                        sugestoes.append(x[-1])
                i = i + 1
            #SUGESTAO PRINCIPAL
            ultimas_palavras = paragrafo_corrente2.split()
            ultimas_palavras = ultimas_palavras[-1]
            i = 0
            while len(bigramasOrd) > i:
                espaco = bigramasOrd[i].rfind(" ")
                if bigramasOrd[i][:espaco] == ultimas_palavras:
                    x = bigramasOrd[i].split()
                    if sugestoes.count(x[-1]) == 0:
                        sugestoes.append(x[-1])
                i = i + 1
            i = 0
            #SUGESTAO USUARIO
            if len(palavrasOrdUser) > 0:
                while len(sugestoes) < 5:
                    sugestoes.append(palavrasOrdUser[i])
                    i = i + 1
            #SUGESTAO PRINCIPAL
            while len(sugestoes) < 5:
                sugestoes.append(palavrasOrd[i])
                i = i + 1
            sugestao = escolher_dentre_sugestoes()
            if sugestao is not None:
                paragrafo_corrente = paragrafo_corrente + " " + sugestao
        elif opcao == 'A':
            if len(texto_corrente) > 0:
                texto_corrente += '\n'
            texto_corrente += paragrafo_corrente
            opcao_novo_paragrafo = input('Deseja iniciar novo parágrafo [N] ou finalizar o texto [F]? ').upper()
            if opcao_novo_paragrafo == 'N':
                paragrafo_corrente = ''
            else:
                break
        elif opcao == 'D':
            opcao_novo_paragrafo = input('Deseja iniciar novo parágrafo [N] ou finalizar o texto [F]? ').upper()
            if opcao_novo_paragrafo == 'N':
                paragrafo_corrente = ''
            else:
                break

    print('----------TEXTO FINAL----------')
    print(texto_corrente)
    opcao_adicionar_base = input('\nDeseja adicionar o texto a base de textos do usuário? [S/N] ').upper()
    if opcao_adicionar_base == 'S':
        file3 = open('corpus usuario.txt', 'r')
        conteudo = file3.readlines()
        conteudo.append(texto_corrente)
        conteudo = "\n".join(conteudo)
        file3 = open('corpus usuario.txt', 'w')
        file3.writelines(conteudo)
        file3.close()
        print('Texto adicionado com sucesso!')


def main():
    print('Bem vindo ao editor mais simples possível!')
    while True:
        print('\nO que você deseja fazer?')
        print('[I] - Iniciar novo texto')
        print('[E] - Encerrar o programa')
        print('[APAGAR] - Apagar os dados do usuário e restaurar as configurações de fábrica')
        opcao = input('Opção: ').upper()
        if opcao == 'I':
            sugestoes.clear()
            iniciar_novo_texto()
        elif opcao == 'E':
            encerar_programa()
        elif opcao == 'APAGAR':
            apagar_dados()


if __name__ == '__main__':
    main()