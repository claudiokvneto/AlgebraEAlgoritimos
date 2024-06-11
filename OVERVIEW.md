Questão:

Uma antiga máquina de escrever permite que, em uma folha de papel A4 com uma
configuração de margem padrão, sejam digitados 50 caracteres por linha. Considerando que
não haverá separação de uma palavra em mais de uma linha, ou seja, caso o tamanho da
última palavra seja maior que o espaço restante, a linha ficará com menos de 50 caracteres,
desenvolva um programa que receba do usuário o texto que será digitado e exiba como saída:
• Quantos caracteres terão em cada linha do texto.
• Quantas linhas foram necessárias para acomodar o texto.

Desenvolvimento da Atividade:

funcao.py
main.py
testes.py

funcao.py:
É responsável por calcular o número de linhas necessárias para exibir um texto, dado 
um limite de 50 caracteres por linha.

caracteres_por_linha: define o limite de caracteres por linha (50).
palavras: divide o texto em palavras.
linhas: contador de linhas necessárias.
caracteres_na_linha: contador de caracteres na linha atual.
linhas_texto: lista para armazenar as linhas de texto formatadas.
linha_atual: string para compor a linha atual.

main.py:
Contém a função principal que interage com o usuário, solicitando o 
texto de entrada e exibindo os resultados processados pela função calcular_linhas_caracteres.

testes.py:
Contém testes automatizados para a função calcular_linhas_caracteres, utilizando 
asserções para validar os resultados.

Testes automatizados:

Teste para texto vazio:
Verifica se a função retorna corretamente quando o texto é vazio.

Teste para linhas com no máximo 50 caracteres:
Verifica se a função lida corretamente com um texto que tem exatamente 50 caracteres.

Resumo
funcao.py: Define a função para calcular linhas e caracteres de um texto.
main.py: Interage com o usuário para obter texto, calcula e exibe os resultados.
testes.py: Contém testes automatizados para validar a função calcular_linhas_caracteres.
