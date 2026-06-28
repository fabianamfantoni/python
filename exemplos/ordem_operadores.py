#Informações -> docs -> 2-ordem-operadores.md

#----------1º - Operadores Aritméticos----------
#----------Segue a ordem matemática.-----------


resultado = (2 + 3) * 4 # Parênteses 
print(resultado)   # 20 sem o parênteses: 2 + 3 * 4 = 14 

exponenciacao = 2 ** 3
print(exponenciacao)   # 8

exponenciacao = 2 ** 3 ** 2
print(exponenciacao)   # 512 (equivale a 2 ** (3 ** 2))

a = 10
b = 3

print(a * b)    # 30 multiplicação
print(a / b)    # 3.333... divisão real(com virgula/ponto)
print(a // b)   # 3 divisão inteira
print(a % b)    # 1 resto da divisão (sobra da divisão)

#QUANDO TODOS OS OPERADORES TEM A MESMA PRECEDÊNCIA SEGUE SE DA ESQUERDA PARA A DIREITA ->

print(a + b - a)   # 10 + 3 -> 13 - 10 = 3  soma/subtração  


#-----------2º - Operadores de Comparação-----------
#------compara dois valores------
print(a < b)# verifica se 10 é menor que 3. RESULTADO: False.
print(a <= b) # Menor ou igual.     RESULTADO: False.
print(a > b)  # Maior.              RESULTADO: True.
print(a >= b) # Maior ou igual.     RESULTADO: True.
print(a == b) # Igual.              RESULTADO: False.
print(a != b) # Diferente.          RESULTADO: True.

#-----------3º - Operadores Lógicos-----------
#Em processos do dia a dia True: verdadeiro(confimando a ação)/False:Falso(cancela a ação)

#-----and - ambos verdadeiros para resultar em True 
c = 5
d = 10

print(c > 0 and d > 0)   # True (ambos maiores que 0)
print(c > 0 and d < 0)   # False (segunda condição é falsa)

#ex.: login

usuario_correto = True
senha_correta = True

if usuario_correto and senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")

#-----or - True se pelo menos uma das condições for verdadeira.

print(a > 0 or b > 11)   # True (a > 0 é verdadeiro)
print(a < 0 or b < 11)   # True (b < 11 é verdadeiro)
print(a < 0 or b > 11)   # False (nenhuma condição é verdadeira)

#ex.: mensagem

num_telefone = False
email = True

# Usando OR
if num_telefone or email:
    print("Mensagem enviada!")

#-----not - inverte o valor lógico.

ativo = True
print(not ativo)   # False (inverteu o valor)

numero = 5
print(not numero > 0)   # False (pois numero > 0 é True, e o not inverte)


#ex.: lâmpada

# True = acesa, False = apagada.
lampada = True  
print("Estado inicial. Acesa: ", lampada) # True 

# Usando not para inverter.
lampada = not lampada # inverte o valor e salva false na variável lampada
print("Depois do not. Acesa: ", lampada) # False 

lampada = not lampada
print("Depois do segundo not. Acesa: ", lampada) # True /acesa novamente ja que os valores salvos foram alterados de  true-> false-> true.

#-----------4º - Operadores de Atribuição-----------

# = ->  atribuição simples
x= 10

#  +=   -> soma e reatribui
x += 3   # 13 equivalente a x = x + 3

#  -=   -> subtrai e reatribui
x -= 4   #9 equivalente a x = x - 4

#  *=   -> multiplica e reatribui
x *= 2   # 18 equivalente a x = x * 2

print(x)# resultado final de todas as alterações(atribui de cima para baixo x começa com 10 -> 13 -> 9->18 )

y = 50
#  /=   -> divide e reatribui
y /= 5   #10 equivalente a x = x / 5

#  //=  -> divisão inteira e reatribui
y //= 3   # 3 equivalente a x = x // 3
print(y)#3.0

z = 20
#  %=   -> resto da divisão e reatribui
z %= 7  # 6 equivalente a x = x % 7 (20/7 = 2 com resto 6)

#  **=  -> eleva a potência e reatribui
z **= 4   # equivalente a x = x ** 4

print(z)   # 20 -> 6*6*6*6-> R:1296


#----------5º - Operadores Bit a Bit----------

num1 = 6   # binário: 110
num2 = 3   # binário: 011

# &  -> AND binário: 1 apenas se ambos os bits forem 1.
print(num1 & b)  # 2 (binário: 010)

# |  -> OR binário:retorna 1 se pelo menos um dos bits for 1.
print(num1 | b)   # 7 (binário: 111)

# ^  -> XOR binário:retorna 1 se os bits forem diferentes.
print(num1 ^ b)   # 5 (binário: 101)

# ~  -> NOT binário:inverte todos os bits (complemento de dois).
print(~num1)   # -7

# << -> deslocamento à esquerda:desloca os bits para a esquerda, multiplicando por 2 a cada posição.
print(num1 << 1)   # 12 (binário: 1100)


# >> -> deslocamento à direita: desloca os bits para a direita, dividindo por 2 a cada posição.

print(num1 >> 1)   # 3 (binário: 11)

