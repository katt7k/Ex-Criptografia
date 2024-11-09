from itertools import permutations

def quebra_transposicao_sem_chave(texto_cifrado, max_comprimento_chave):
    possiveis_decifrados = []  # Lista para armazenar os possíveis textos decifrados

    # Testar todos os comprimentos de chave possíveis, começando de 2 até o valor máximo especificado
    for comprimento_chave in range(2, max_comprimento_chave + 1):
        num_colunas = comprimento_chave  # Número de colunas para o comprimento atual da chave
        num_linhas = len(texto_cifrado) // num_colunas  # Calcula o número de linhas necessárias
        
        # Ignorar se o texto não divide exatamente 
        if len(texto_cifrado) % num_colunas != 0:
            continue  # Se não dá para dividir certinho, vamos para o próximo comprimento
        
        print(f"\nTestando com comprimento de chave: {comprimento_chave}")
        
        # Para cada possível ordem de colunas (ou seja, cada permutação) do comprimento atual
        for permutacao in permutations(range(num_colunas)):
            texto_decifrado = [""] * len(texto_cifrado)  # Inicializa a lista para o texto decifrado
            pos = 0  # variável para ajudar a percorrer cada letra do texto cifrado
            
            # Construir a "matriz" de acordo com a permutação de colunas
            # Cada coluna da permutação nos diz a ordem de leitura para decifrar
            for coluna in permutacao:
                for linha in range(num_linhas):
                    # Calcula a posição correta na lista onde cada letra deve ir
                    index = linha * num_colunas + coluna
                    texto_decifrado[index] = texto_cifrado[pos]
                    pos += 1  # Avança para a próxima letra do texto cifrado
            
            # Juntar todas as letras em uma string só, que é nosso texto decifrado com essa permutação
            texto_decifrado = ''.join(texto_decifrado)
            possiveis_decifrados.append(texto_decifrado)  # Guarda essa tentativa na lista de resultados
            print(f" {permutacao}: {texto_decifrado}")

    return possiveis_decifrados  # Retorna todos os textos decifrados para análise 

resultados = quebra_transposicao_sem_chave("UIIXQOLAESNXCADX" , 5)
