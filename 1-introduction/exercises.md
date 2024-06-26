# Exercícios Capítulo 1 - Introdução

## Questões:

1. Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

2. Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?

3. Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica.

4. Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica. (Dica: Deve procurar pela agenda inteira!)

5. Você quer ler o número de cada pessoa da agenda telefônica.

6. Você quer ler os números apenas dos nomes que começam com A.

## Respostas:

1. 128 nomes resultam em **7 etapas**, pois $\log_2 128$ = 7

2. 256 nomes resultam em **8 etapas**, pois $\log_2 128$ = 8

3. O($\log_2 n$)

4. O(n)

5. O(n)

6. Intuitivamente, pensamos em O(n/26), pois estamos fazendo a busca em apenas 1 dos 26 caracteres, porém uma das regras da notação Big O é ignorar números que são somados, subtraídos, multiplicados ou divididos, para simplificar a notação, então devemos ignorar a divisão por 26 e consequentemente temos o resultado **O(n)**