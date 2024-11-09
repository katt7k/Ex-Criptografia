from collections import Counter

def decifrar_por_frequencia(texto_cifrado, letras_alvo=["A", "E", "I", "O", "R", "S", "U"]):
    # Conta a frequência de cada caractere no texto cifrado
    quantidade = Counter(texto_cifrado)
    
    # Seleciona o caractere mais comum no texto cifrado
    comum_tc = quantidade.most_common(1)[0][0]
    print(f"Letra mais comum no texto cifrado: {comum_tc}")
    
    # Tenta decifrar o texto usando cada letra da lista de letras_alvo como possível letra mais comum
    for letra in letras_alvo:
        texto_decifrado = ""
        
        # Calcula a chave com base na diferença entre o caractere mais comum e a letra-alvo
        if comum_tc.isupper():
            # Se for maiúscula, calcula a chave para alinhar o caractere mais comum com a letra-alvo
            chave = ord(comum_tc) - ord(letra.upper())
        elif comum_tc.islower():
            # Se for minúscula, ajusta a chave para letras minúsculas
            chave = ord(comum_tc) - ord(letra.lower())
        
        print(f"\nTentativa com a letra-alvo '{letra}' como mais comum:")
        print(f"Chave calculada: {chave}")
        
        # Usa a chave calculada para decifrar cada caractere do texto cifrado
        for i in texto_cifrado:
            if i.isupper():
                # Para letras maiúsculas, aplica a chave para retornar ao texto original
                texto_decifrado += chr((ord(i) - chave - 65) % 26 + 65)
            elif i.islower():
                # Mesma lógica acima, mas para letras minúsculas
                texto_decifrado += chr((ord(i) - chave - 97) % 26 + 97)
            else:
                # Se não é letra (espaços, pontuações), adiciona sem modificação
                texto_decifrado += i 
        
        # Exibe o resultado da decifração com a letra-alvo atual
        print(f"Texto decifrado: {texto_decifrado}")
decifrar_por_frequencia("pdqxhod")
