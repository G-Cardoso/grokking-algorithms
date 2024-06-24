# Entendendo Algoritmos: 
### Um guia ilustrado para programadores e outros curiosos

## Capítulo 1 - Introdução a algoritmos
### Introdução
**Algoritmos** são conjunto de intruções que realizam uma determinada tarefa.

### Notação Big O
É uma notação que demonsta o quão rápido é um algoritmo, sendo necessária para realizar comparações com outros algoritmos.
Existem diversos tempos de execução, mas os principais (em ordem de velocidade) são:
1. O(1) - Tempo constante
2. O(log n)
3. O(n)
4. O(n log n)
5. O(n²)
6. O(n!)

*Considere **n** como o número de operações, pois um algortimo não é medido pelo tempo mas sim pelo crescimento do número de operações, pois o tempo é variável conforme a arquitetura do computador, hardware, dentre outras coisas.

E seus respectivos gráficos:

IMG


### Pesquisa Binária (Binary Search)
Diferente do método de pesquisa clássico (sequencial), onde dada uma lista ordenada, vamos procurar elemento por elemento até encontrar o que queríamos, na **Busca Binária** conseguímos reduzir o tempo de pesquisa, sempre iniciando a busca pelo meio da lista e descobrindo se encontramos o item, se está "para frente" ou se está "para trás", reduzindo o número de operações (considerando pior caso e caso médio).

#### Tempo de execução:
##### Pesquisa Clássica (Sequencial):
Como pesquisamos item por item, ordenados, considerando o pior caso, vamos precisar realizar **n** operações, onde **n** é a quantidade de elementos da lista, então temos O(n), ou seja, em uma lista com 1 bilhão de elementos, vamos precisar realizar 1 bilhão de operações.

##### Pesquisa Binária:
Neste caso, começamos a pesquisa pela metade da lista, depois a metade da metade, depois a metade da metade da metade e assim sucessivamente, então considerando o pior caso, vamos precisar realizar **$ \log_2 n $** operações, onde **n** é a quantidade de elementos da lista, então temos O($ \log_2 n $), ou seja, em uma lista com 1 bilhão de elementos, vamos precisar realizar apenas 30 operações.


