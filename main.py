from funcao import calcular_linhas_caracteres

def main():
    texto = input("Digite o texto: ")
    total_caracteres, caracteres_por_linha, linhas, linhas_texto = calcular_linhas_caracteres(texto)

    print(f"Total de caracteres: {total_caracteres}")
    print(f"Linhas necessárias: {linhas}")
    print("\nTexto formatado:")
    for linha in linhas_texto:
        print(linha)

if __name__ == "__main__":
    main()
