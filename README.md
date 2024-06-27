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

![image](https://github.com/G-Cardoso/Grokking-Algorithms/assets/30526226/b8e55480-edb4-403c-9c4d-df9cfe06db06)

### Pesquisa/Busca Binária (Binary Search)
Diferente do método de pesquisa clássico (sequencial), onde dada uma lista ordenada, vamos procurar elemento por elemento até encontrar o que queríamos, na **Busca Binária** conseguímos reduzir o tempo de pesquisa, sempre iniciando a busca pelo meio da lista e descobrindo se encontramos o item, se está "para frente" ou se está "para trás", reduzindo o número de operações (considerando pior caso e caso médio).

#### Tempo de execução:
##### Pesquisa Clássica (Sequencial):
Como pesquisamos item por item, ordenados, considerando o pior caso, vamos precisar realizar **n** operações, onde **n** é a quantidade de elementos da lista, então temos O(n), ou seja, em uma lista com 1 bilhão de elementos, vamos precisar realizar 1 bilhão de operações.

##### Busca Binária:
Neste caso, começamos a pesquisa pela metade da lista, depois a metade da metade, depois a metade da metade da metade e assim sucessivamente, então considerando o pior caso, vamos precisar realizar **$\log_2 n$** operações, onde **n** é a quantidade de elementos da lista, então temos O($\log_2 n$), ou seja, em uma lista com 1 bilhão de elementos, vamos precisar realizar apenas 30 operações.

Código da **Busca Binária** disponível em: [binary_search.py](1-introduction/binary_search.py)

#### Exercícios
Exercícios do Capítulo 2 estão disponíveis [aqui](1-introduction/exercises.md)

## Capítulo 2 - Ordenação por Seleção

### Memória do Computador
A Memória de um computador é semelhante à um enorme gaveteiro, onde cada gaveta (posição da memória) possui um endereço único e pode armazenar um objeto (bytes de dados).

### Arrays
Array é uma estrutura de dados onde as informações são salvas na memória do computador de maneira **sequencial e contínua**, ou seja, se eu desejo salvar 10 objetos de 2 bytes cada, terei na memória, uma sequência de 20 bytes contínuos, representados na imagem abaixo:

IMAGEM PAINT

Sabendo a posição inicial do Array (endereço de memória), o tamanho de cada objeto (em bytes) eu consigo acessar qualquer elemento da lista.
Por exemplo, se eu desejo acessar o elemento 4 da lista que criamos anteriormente, basta fazer ENDEREÇO_DE_MEMORIA + (4 * TAMANHO_DO_OBJETO).

**Inserção $O(n)$:** Pensando no pior caso, onde não houver espaço de memória livre para novas inserções, é necessário alocar novos espaços na memória e mover os dados anteriores.  
**Leitura $O(1)$:** O acesso às informações é aletório (como discutimos acima), portanto posso acessar qualquer elemento do array "instantaneamente".  
**Remoção $O(n)$:** Quando um elemento é removido, eu preciso reoganizar os outros **$n$** elementos para ficarem de maneira contínua na memória.

### Listas Encadeadas (Linked List)
Diferente dos Arrays, a Lista Encadeada não precisa ser salva de maneira contínua, **aproveitando melhor os espaços de memória**. Cada elemento salvo possui um campo que aponta para o endereço do próximo elemento, ou para o elemento anterior, dependendo da maneira como foi implementada.

IMAGEM LIVRO (pg 44)

**Inserção $O(1)$:** Para adicionar um item a uma lista encadeada é simples, basta colocar em qualquer lugar da memória e armazenar o endereço do item anterior.  
**Leitura $O(n)$:** É necessário fazer uma leitura sequencial, ou seja, para chegar no elemento **$n$** devemos ler todos os elementos anteriores.  
**Remoção $O(1)$:** Ao remover um elemento, basta "reoganizar" a lista, trocando o campo do elemento anterior e/ou do próximo elemento.

### Arrays vs Listas Encadeadas

IMAGEM LIVRO (pg 48)

Como podemos ver na imagem acima, devemos escolher um ou outro de acordo com cada caso.  
Por exemplo, se o problema requer **muita leitura** e **pouca inserção**, o vencedor será **Array**  
Já se o programa requer pouca leitura e muita inserção, o vencedor será **Listas Ligadas**  
*Obs: Há outras estruturas de dados mais adequadas, com tempo médio melhores, mas é assunto para os próximos capítulos.

### Ordenação por Seleção (Selection Sort)
Uma das maneiras mais intuitivas e naturais de realizar uma ordenação é a Ordenação por Seleção.  
Você seleciona um elemento, compara com todos os outros e salva em uma nova lista.

Aqui está um **exemplo**:
1. Uma lista com os elementos [7, 9, 2, 55, 24]  
2. Primeiro pegamos o primeiro elemento da lista, nesse caso, o 7 e comparo ele com os demais.  
3. Se 7 for MAIOR que o próximo elemento, continuamos com 7, caso contrário, trocamos de número.  
4. Nesse caso, trocamos para o 9, e fazemos novamente a comparação com o próximo.  
5. Seguindo esse passo, vamos ter que o maior elemento dessa lista é o 55.  
6. Após encontrar o menor elemento, coloco-o em uma nova lista e removo da lista anterior, ou seja, agora temos duas listas, a primeira é [7, 9, 2, 24] e a segunda é [55].  
7. Agora vou repetir o processo com a primeira lista [7, 9, 2, 24] até que a lista fique vazia.  
8. Ao final, teremos a primeira lista [] (vazia) e a segunda lista com os elementos ordenados [55, 24, 9, 7, 2].  
*Obs: Para ordenar em ordem decrescente, basta trocar o passo **3** para considerar o MENOR elemento, assim, teremos o resultado final em ordem decrescente .

IMAGEM LIVRO (pg 53)

Como podemos ver pelo exemplo e imagem acima, fizemos 2 operações.  
Para encontrar o menor elemento, fizemos **$n$** comparações **$n$** vezes, ou seja, nosso tempo de execução é **$O(n*n)$** ou **$O(n^2)$**.

Código da **Ordenação por Seleção** disponível em: [selection_sort.py](2-selection_sort/binary_search.py)

#### Exercícios
Exercícios do Capítulo 2 estão disponíveis [aqui](2-selection_sort/exercises.md)