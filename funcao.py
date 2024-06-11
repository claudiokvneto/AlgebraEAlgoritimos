def calcular_linhas_caracteres(texto):
    caracteres_por_linha = 50
    palavras = texto.split()
    linhas = 0
    caracteres_na_linha = 0
    linhas_texto = []
    linha_atual = ""

    for palavra in palavras:
        if caracteres_na_linha + len(palavra) + (1 if caracteres_na_linha > 0 else 0) > caracteres_por_linha:
            linhas += 1
            linhas_texto.append(linha_atual.rstrip())
            linha_atual = ""
            caracteres_na_linha = 0

        while len(palavra) > caracteres_por_linha:
            linhas += 1
            linhas_texto.append(palavra[:caracteres_por_linha])
            palavra = palavra[caracteres_por_linha:]

        linha_atual += palavra + " "
        caracteres_na_linha += len(palavra) + 1

    if caracteres_na_linha > 0:
        linhas += 1
        linhas_texto.append(linha_atual.rstrip())

    total_caracteres = len(texto)
    
    return total_caracteres, caracteres_por_linha, linhas, linhas_texto
