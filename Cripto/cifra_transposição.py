def cifra_transposicao(texto, chave):
    # Remover espaços e ajustar o texto
    texto = texto.replace(" ", "")
    
    # Definir a permutação com base na ordem alfabética da chave
    ordem_chave = sorted(range(len(chave)), key=lambda x: chave[x])
    
    # Calcular o número de linhas necessárias
    num_colunas = len(chave)
    num_linhas = (len(texto) + num_colunas - 1) // num_colunas
    
    # Preencher a grade com o texto
    grade = [""] * num_linhas
    for i in range(num_linhas):
        grade[i] = texto[i * num_colunas:(i + 1) * num_colunas]
    
    # Adicionar x se necessário
    if len(grade[-1]) < num_colunas:
        grade[-1] += "X" * (num_colunas - len(grade[-1]))

    # Construir o texto cifrado lendo as colunas na ordem da chave
    texto_cifrado = ""
    for indice in ordem_chave:
        for linha in grade:
            texto_cifrado += linha[indice] if indice < len(linha) else ""
    
    return texto_cifrado
texto_cifrado = cifra_transposicao("QUE COISA LINDA", "MANU")
print("Texto Cifrado:", texto_cifrado)
