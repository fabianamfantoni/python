# :round_pushpin: Introdução ao Python


*Python, diferente de outras linguagens que são mais verbosas, apresenta uma sintaxe mais simplificada e intuitiva. Essa característica torna o aprendizado mais prático e a escrita de código mais clara, focado mais na lógica.*

*A lógica, como um todo, nos ajuda a enxergar as situações de maneira mais clara e objetiva.É por meio dela que os programadores,  independentemente da linguagem, conseguem resolver os problemas no seu dia a dia.*

---

## :warning: Indentação 

**Identação**: *é o ato de inserir espaços ou recuos no início de uma linha de código.*

***Em Python é extremamente importante, não apenas por deixar o código organizado e bonito, mas porque, sem a identação correta, o código não funciona, já que indica onde começam e terminam os blocos (condições, laços, funções, classes). ***

---

## :bulb: Tipagem Dinâmica
 
*Em linguagens como Java ou C++, é necessário declarar o tipo da variável (ex.: int idade = 25;). Já em Python, o tipo é dedusido automaticamente pelo interpretador no momento da atribuição. Isso significa que o programador não precisa especificar se é inteiro, string ou float — o Python reconhece sozinho.*


**Consequências da Tipagem Dinâmica:**

- Flexibilidade: facilita a escrita rápida de código.
- Risco de erros lógicos: como o tipo pode mudar durante a execução, é possível sobrescrever variáveis com tipos diferentes.

- Comparação: em C ou Java, isso não seria permitido sem conversão explícita.Ex.: String nome = "Maria";


**Type Hints**

:point_up:*A ausência de declaração explícita de tipos é um dos fatores que tornam Python mais simples. Porém, exige do programador consistência para manter e evitar erros. Em ambientes maiores, recomenda-se o uso de **type hints** (anotações de tipo) para aumentar a legibilidade e segurança.*

---

## :card_file_box: Sintaxe Básica

*Alguns pontos importantes em comparação com outras linguagens:*

- **.**(*ponto*): usado para acessar métodos e atributos de objetos.

- **[]** (*colchetes*): utilizados para listas, acesso a índices e fatias.
> :paperclip: O fatiamento (ou slicing) em Python é uma técnica para extrair partes de sequências (como strings, listas e tuplas) usando a notação de colchetes e dois pontos. Ex.: nomeLista[início:fim:passo]

- **()** (*parênteses*): empregados em chamadas de funções e definição de tuplas.

- **" * "** (*asterisco*): usado para multiplicação, repetição de sequências e desempacotamento de argumentos.*" * "(para iteráveis) e " * * " (para dicionários)*

- **{}** (*chaves*): delimitam dicionários e conjuntos.

- **'**(*aspas simples*) ou **"** (*aspas duplas*) : definem strings.

- **:**(dois pontos): marcam blocos de código (*condições, laços, funções, classes*).

*Essa ausência de símbolos redundantes, como ; ao final das linhas, diferencia Python de linguagens como Java ou C++.*

---

## :building_construction: Estruturas Fundamentais

- **Variáveis:** são espaços de memória onde guardamos valores.
- **Constantes:** python não possui constantes nativas, mas por convenção são usados nomes em maiúsculas.Ex.: PI = 3.14159
- **Função:** permitem modularizar o código e reutilizar lógica indefinidamente. 
- **Classes:** são moldes para criar objetos.
- **Métodos:** são como "ações" ou "operações" que um objeto sabe realizar, são definidos dentro de uma classe e podem manipular os atributos(variáveis internas), ou executar tarefas específicas.
    - Tipos de Métodos:
    1. Método de instância: atua sobre o objeto criado.
    2. Método de classe: atua sobre a classe em si.
    3. Método estático: não depende da instância nem da classe.

- **Comentários:**servem para documentar o código.

---

``` 
# Este é um comentário de linha

"""
Este é um comentário
de múltiplas linhas
"""

```

---

- **Concatenação:**é a união de strings ou valores. Podem ser com:
    - **+**:usa o operador de adição para unir strings e também funciona para unir listas.
    - **join()**: Método para unir elementos de uma lista em uma única string.
    - **f-strings**: permite inserir variáveis diretamente dentro de uma string.
    - **format()**: Método mais antigo, pouco usado para interpolar valores em strings.
    - **%**(*Interpolação antiga*):  Estilo herdado de C, menos usado hoje em dia.

---

nerd_face: ***Python é uma linguagem que foca na clareza e na produtividade. Sua sintaxe simplificada, torna-a ideal tanto para iniciantes quanto para profissionais que desejam desenvolver de forma ágil.***