from funcao import calcular_linhas_caracteres

def testar_calcular_linhas_caracteres():
    # Teste 1: Frase padrão
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    total_caracteres, caracteres_por_linha, linhas, linhas_texto = calcular_linhas_caracteres(texto)
    assert total_caracteres == 56, f"Falha no teste 1: esperado 56, obtido {total_caracteres}"
    assert caracteres_por_linha == 50, f"Falha no teste 1: esperado 50, obtido {caracteres_por_linha}"
    assert linhas == 2, f"Falha no teste 1: esperado 2, obtido {linhas}"
    assert linhas_texto == ["Lorem ipsum dolor sit amet, consectetur adipiscing", "elit."], f"Falha no teste 1: esperado ['Lorem ipsum dolor sit amet, consectetur adipiscing', 'elit.'], obtido {linhas_texto}"
    
    # Teste 2: Linha exata de 50 caracteres
    texto = "a" * 50
    total_caracteres, caracteres_por_linha, linhas, linhas_texto = calcular_linhas_caracteres(texto)
    assert total_caracteres == 50, f"Falha no teste 2: esperado 50, obtido {total_caracteres}"
    assert caracteres_por_linha == 50, f"Falha no teste 2: esperado 50, obtido {caracteres_por_linha}"
    assert linhas == 1, f"Falha no teste 2: esperado 1, obtido {linhas}"
    assert linhas_texto == ["a" * 50], f"Falha no teste 2: esperado ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'], obtido {linhas_texto}"
    
    # Teste 3: Várias linhas quase completas
    texto = "a " * 49 + "a"
    total_caracteres, caracteres_por_linha, linhas, linhas_texto = calcular_linhas_caracteres(texto)
    assert total_caracteres == 99, f"Falha no teste 3: esperado 99, obtido {total_caracteres}"  # Ajustado para 99
    assert caracteres_por_linha == 50, f"Falha no teste 3: esperado 50, obtido {caracteres_por_linha}"
    assert linhas == 2, f"Falha no teste 3: esperado 2, obtido {linhas}"
    assert linhas_texto == ["a " * 24 + "a", "a " * 24 + "a"], f"Falha no teste 3: esperado ['a ' * 24 + 'a', 'a ' * 24 + 'a'], obtido {linhas_texto}"
    
    print("Todos os testes passaram!")

if __name__ == '__main__':
    testar_calcular_linhas_caracteres()
