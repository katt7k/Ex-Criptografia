def criptografar(palavra, chave=3):
    # Inicializa uma variável para armazenar o texto cifrado
    cifrada = ""
    
    # Percorre cada caractere da palavra
    for n in palavra: 
        # Verifica se o caractere é uma letra maiúscula
        if n.isupper(): 
            # Se for maiúscula, calcula a posição cifrada usando a fórmula da Cifra de César:
            # - Converte a letra para um número (ord(n))
            # - Soma a chave para "deslocar" a letra
            # - Subtrai 65 para ajustar ao início do alfabeto (A=0, B=1, etc.)
            # - Usa o módulo 26 para manter o deslocamento dentro do alfabeto (de A a Z)
            # - Soma 65 para retornar ao código ASCII da nova letra maiúscula
            cifrada += chr((ord(n) + chave - 65) % 26 + 65) 
        
        # Verifica se o caractere é uma letra minúscula
        elif n.islower(): 
            # Mesma lógica de cima, mas ajustada para letras minúsculas:
            # Subtrai 97 para alinhar com 'a' = 0, 'b' = 1, etc.
            # Soma 97 no final para voltar ao código ASCII de letras minúsculas
            cifrada += chr((ord(n) + chave - 97) % 26 + 97)
        
        # Se o caractere não é letra (ex: espaço, pontuação), ele é mantido como está
        else: 
            cifrada += n 
    print(cifrada)

criptografar('manuela')
