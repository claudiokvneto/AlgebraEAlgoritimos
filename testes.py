from funcao import calcular_linhas_caracteres

def testar_calcular_linhas_caracteres():

    #Validação para textos vazios.
    texto = ""
    total_caracteres, caracteres_por_linha, linhas, linhas_texto = calcular_linhas_caracteres(texto)
    assert total_caracteres == 0, "Falha no teste 1: Texto vazio"
    assert linhas == 0, "Falha no teste 1: Texto vazio"
    assert linhas_texto == [], "Falha no teste 1: Texto vazio"

    print("Teste para texto vazio passou!")

    #Validação para linhas com no maximo 50 caracteres
    texto = "a" * 50
    total_caracteres, caracteres_por_linha, linhas, linhas_texto = calcular_linhas_caracteres(texto)
    assert total_caracteres / linhas <= 50, 'Falha no teste 2: Linha com mais de 50 caracteres'

    print("Teste para total de caracteres passou!")

if __name__ == '__main__':
    testar_calcular_linhas_caracteres()
