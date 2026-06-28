# :mechanical_arm: Operadores

*Os operadores permitem realizar cálculos, comparações, atribuições e manipulações de dados. Eles são fundamentais para controlar a lógica e o fluxo dos programas.*

*Toda linguagem de programação segue uma ordem de precedência que deve ser seguida para que os programas sejam executados corretamente, em python não seria diferente.*

**Os principais operadores são : operadores aritméticos, operadores de comparação e operadores lógicos.**

---

## **1º - Operadores Aritméticos** 

*Usados para realizar cálculos matemáticos, são aplicados quando precisamos manipular valores numéricos em expressões matemáticas ou em programas que envolvem cálculos.*

- Ordem de precedência(leitura): 
    1. () → Parênteses
    2. ** → Exponenciação
    3. *, /, //, % → Multiplicação, Divisão, Divisão inteira e Módulo
    4. +, - → Soma e Subtração

---

## **2º - Operadores de Comparação** 

*Verificam relações entre valores, são usados em estruturas condicionais (if, while...) para tomar decisões com base em comparações lógicas.*

- Ordem de precedência(leitura): 

    1. **<**  | Menor          |
    2. **<=** | Menor ou igual |
    3. **>**  | Maior          |
    4. **>=** | Maior ou igual |
    5. **==** | Igual          |
    6. **!=** | Diferente      |

---

## **3º - Operadores Lógicos**

*Servem para controlar o fluxo lógico de decisões. Eles são usados principalmente para combinar ou inverter resultados booleanos.*

- Ordem : 
    1. and → verdadeiro se ambos forem verdadeiros. Ex.:confirmação de senhas e usuario.
    2. or → verdadeiro se pelo menos um for verdadeiro. Ex.: Envio de mensagem. num_telefone: False,email: True. envia a mensagem para o email.
    3. not → inverte o valor lógico. True -> False/False -> True. Ex.: lâmpada

---

### :handshake: Outros tipos são: 

- **4º - Operadores de Atribuição:** *são usados para atribuir valores a variáveis, podendo incluir operações junto da atribuição. Funcionan como "shorthand" ao atualizar valores sem precisar reescrever a variável.*

    | =   |atribuição simples |
    |atribuição com operação: calcula -e salva o resultado na variavel|
    | +=  | soma um valor à variável e reatribui o resultado.
    | -=  | subtrai um valor da variável.
    | *=  | multiplica a variável.
    | /=  | divide a variável.
    | //= | faz a divisão inteira.
    | %=  | calcula o resto da divisão.
    | **= | eleva a variável a uma potência e reatribui.

> ex.: k = 10/ k+=2 #k vale 12 apos o calculo

- **5º - Operadores Bit a Bit:** *operam diretamente nos bits dos números inteiros. Usados em programação de baixo nível, manipulação de dados binários e otimizações.*
    **&** =  AND binário, ambos '1'.
    **|** = OR binário, pelo menos um '1'.
    **^** = XOR binário, bits diferentes.
    **~** = NOT binário, inversão.
    **<<** = deslocamento à esquerda, multiplica.
    **>>** = deslocamento à direita, divide.

---

**Cada tipo de operador em Python tem uma função específica: dos cálculos básicos (aritméticos) às comparações lógicas e manipulação binária. Todos eles formam a base para construir algoritmos e controlar o fluxo dos programas.**

---