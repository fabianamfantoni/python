#Toda linguagem de programação segue uma ordem de precedência dos operadores
    #em python não seria diferente 

## 1º Operadores Aritméticos : 
    # Ordem de precedência(leitura): 
    # () → Parênteses
    # ** → Exponenciação
    # *, /, //, % → Multiplicação, Divisão, Divisão inteira e Módulo
    # +, - → Soma e Subtração

num1 = 10
num2 = 5 

resultado1 = num1 - (4+5)
resultado2 = num2**2 +4 
resultado3 = 1 + 6 - 8 /2 # 1+ 6-(8/2) = 1+6-4

print(f'Calculou ou parênteses primeiro: {resultado1}')
print(f'Calculou a exponenciação primeiro: {resultado2}')
print(f'Calculou a divisão primeiro: {resultado3}')
#Em caso de haver mais de um numero da mesma ordem de precedência(+,- ou *,/,//,%) 
    # o calculo seguira da esquerda para a direita ex: 1+5-2 será (1+5) depois (6-2)

#2º Operadores de Comparação:
    # < → Menor
    # <= → Menor ou igual
    # > → Maior
    # >= → Maior ou igual
    # == → Igual
    # != → Diferente

resultado4 = num1 < num2  #10 é menor que 5 = False
resultado5 = num1 >= num2 #10 é maior ou igual a 5 = True
resultado6 = num1 == num2 #10 é igual a 5 = False
resultado7 = num1 != num2 #10 é diferente de 5 = True

print(f'{resultado4},{resultado5},{resultado6},{resultado7}')

# 3º Operadores Lógicos:
# Servem para controlar o fluxo lógico de decisões. 
# Eles são usados principalmente para combinar ou inverter resultados booleanos.
    # not: Inverte o valor. True vira false/ False vira True ex:

#Criando um dicionário 
usuarios = {
    "José" : "1234",
    "João" : "abcd",
    "Maria" : "senha"
}
#cria uma função contendo dois parâmetros (usuario e senha)
def loggin(usuario,senha):
    # Verifica se o usuário existe:
    if not usuario in usuarios:#"Se o usuário não estiver dentro da lista de usuários"
        print("Usuario não encontrado.")
        return False#"Essa tentativa falhou, pode parar por aqui"

    # Verifica se a senha está correta:
    if not usuarios[usuario] == senha:#"Se a senha digitada não for igual à senha armazenada para esse usuário"
        print("Senha incorreta.")
        return False# "pode parar por aqui"
    
    print("Login realizado com sucesso!")#se tudo estiver correto ele libera o acesso
    return True


    # and:Serve para exigir que duas condições sejam verdadeiras ao mesmo tempo.(caso contrário dará false e não sera executado) 
    
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir") 

    # or: Serve para aceitar que pelo menos uma condição seja verdadeira.(só resulta em false quando as duas condições são falsas)

feriado = False
fim_de_semana = True

if feriado or fim_de_semana:
    print("Dia de descanso")
else:
    print("Dia útil")

