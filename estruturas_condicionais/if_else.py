#Estruturas condicionais if, elif, else, são usadas para tomar decisões dentro do programa, essa sequência é um substituto mais comum para instruções switch case em outras linguagens.

# if : para verificar uma condição única.

idade = 20

if idade >= 18:
    print("Você é maior de idade.\n")

# if + else : quando há duas possibilidades exclusivas. se a primeira for false executa  segunda

guarda_chuva = True

if guarda_chuva == True:
    print("Você esta protegido(a)!")
else:
    print("Você se molhou")

# if + elif + else : quando há várias alternativas possíveis.

nota = 7;

if nota >= 9: #if = condição:
    print("Excelente!")# se a condição for verdadeira, o código executado
elif nota >= 7:#elif: condição 
    print("Bom!") # código executado se a primeira for falsa e essa for verdadeiro
elif nota == 5:
    print("Regular, precisa melhorar") # código executado se a anterior for falsa e essa for verdadeiro
else:
    print("Reprovado(a)")# código executado se nenhuma condição anterior for verdadeira
 
 