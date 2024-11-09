def ataque_forca_bruta(texto_cifrado):
    for chave in range(1, 26):
        texto_decifrado = ""
        for n in texto_cifrado:
            if n.isupper():
                texto_decifrado += chr((ord(n) - chave - 65) % 26 + 65)
            elif n.islower():
                texto_decifrado += chr((ord(n) - chave - 97) % 26 + 97)
            else:
                texto_decifrado += n
        print(f"Chave {chave}: {texto_decifrado}")
ataque_forca_bruta('pdqxhod')

    
