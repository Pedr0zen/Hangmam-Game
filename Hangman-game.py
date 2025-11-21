import random                                  #variaveis
palavras = ['c','python','algoritmos']
sorteio = random.choice(palavras)
underline = ['_'for _ in sorteio]
tentativas = 5
palavras_tentadas = []
def painel():
    print("\n" + '='*30)
    print(('🎮JOGO DA FORCA'.center(26)))
    print('='*30 )
    print(f'Palavra = {''.join(underline)}')
    print(f'Tentativas = {','.join(palavras_tentadas)}')
    print(f'Qtd_de_caracteres = {len(sorteio)} letras')
    print(f'Tentativas = {tentativas}')
    print('='*30 + "\n")
                                                  #Condicoes e logica
while True:
    painel()
    entrada = input('escolha uma palavra:').lower()
    if len(entrada)!= 1 or not entrada.isalpha(): #validacao de apenas uma letra
        print(f'Digite apenas letras (a-z).')
        continue
    if entrada in palavras_tentadas:
        print('voce ja tentou essa letra!')
        continue
    for i, letra in enumerate(sorteio):
            if letra==entrada:             #verificacao da palavra.
                underline[i] = letra       #Atualizacao do Painel.
    if entrada in sorteio:                 #se a palavra for igual a sorteio
        print(f'boa!acertou uma letra')
        print(''.join(underline))
    else:                                  #se nao a palavra for diferente da palavra sorteada, adicione-a numa lista e diminua as chances.
        tentativas-=1
        palavras_tentadas.append(entrada)  #registrar tentativa
        print(f'Nao dessa vez!')

        print(''.join(underline))           #Atualizacao de Status
        print(f'palavras tentadas:{','.join(palavras_tentadas)}')
    if '_' not in underline:                #condicao de fim de Vitoria
        print(f'Voce preencheu tudo! voce venceu!🏆')
        break
    if tentativas <= 0:                     #condicao de fim de Derrota
        print(f'As chances se esgotaram!! voce perdeu!🫵😂')
        break












