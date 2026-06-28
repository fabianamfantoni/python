#Informações -> docs -> 1-basico.md

#---------- Variáveis: ---------- 
# Sintaxe: [variável que armazena][sinal de atribuição"="][valor que será atribuido]

idade = 25   # variável inteira
nome = "Joel" # variável string
altura = 1.50  # variável float

#--------Constantes:--------

PI = 3.14159 

#----------Tipagem Dinâmica----------

nome = "Marta"# String
idade = 25     # inteiro
altura = 1.90   # float
vivo = True      # booleano
#------mudança------
x = 10   # valor inteiro
x = "dez" # x agora é string

#---------- type hints:----------

def soma(a: int, b: int) -> int:
    return a + b

#-----------Funções-----------

def saudacao(nome): 
    return f"Olá, {nome}!"

print(saudacao("Mirian"))   # Olá, Mirian!

#-----------Classe:-----------

class Pessoa: # Definição da Classe
    def __init__(self, nome, idade): #Método Especial __init__(É o construtor da classe)
        self.nome = nome # self. Atributos da Instância
        self.idade = idade # O prefixo self. indica que pertencem à instância e não são variáveis locais.

#----------Métodos----------

class Calculadora:
    def soma(self, a, b):          # método de instância
        return a + b

    @classmethod
    def descricao(cls):            # método de classe
        return "Classe de cálculo"

    @staticmethod
    def multiplicar(a, b):         # método estático
        return a * b


#----------exemplo de uso da classe pessoa----------

p1 = Pessoa("Maria", 25) #classes e métodos  podem ser reutilizados indefinidamente
print(p1.nome)   # Maria
print(p1.idade)  # 25

p2 = Pessoa("Jorel", 22)
print(p2.nome)   # Jorel
print(p2.idade)  # 22
