# A lógica, como um todo, nos ajuda a enxergar as situações de maneira mais clara e objetiva. 
# E na programação não poderia ser diferente, é ela que ajuda a enxergar os problemas do dia a dia em partes a serem resolvidas.

# Estruturas básica: 

# Variáveis: São espaços de memória onde guardamos valores.
# Sintaxe: [variável que armazena][sinal de atribuição"="][valor que será atribuido]
usuario = "Joel"
idade = 18
print(f"Olá {usuario} você têm {idade} anos!")
# Em Python, você não precisa declarar o tipo da variável. 
# O interpretador descobre automaticamente o tipo com base no valor atribuído.

#Operadores: Permitem realizar cálculos ou comparações.
somar = 5 + 5
maior = somar > 5 
print(f'Sua soma resultou em {somar}, esse valor é maior que 5? R:{maior}!!')

#Condicionais: Usadas para a tomada de decisões. Se o primeiro parâmetro não ocorre, ele executa outro.
if idade >= 18:
    print(f"{usuario} Você é maior de idade")#Retorna a mensagem se o valor na idade for igual ou maior de 18.
else:
    print(f"{usuario} Você é menor de idade")#Retorna a mensagem se o valor na idade for menor de 18

#Laços de repetição: Executam ações repetidamente.
# SEMPRE COLOCAR UM PONTO DE PARADA(break) OU PARÂMETRO LIMITE (nesse caso o range(5)) PARA EVITAR LOOPS INFINITOS.
for i in range(5):#inicia uma contagem em 0 e executa até o 5º valor(0,1,2,3,4)  
    print(i)

# Funções: Agrupam blocos de código reutilizáveis.

def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao("Maria"))

#A lógica básica se conecta diretamente com problemas práticos:
#Automatização de tarefas: Criar scripts para organizar arquivos, enviar e-mails ou processar dados.
#Análise de dados: Usar estruturas lógicas para filtrar, calcular e interpretar informações.
#Controle de fluxo: Decidir o que o programa deve fazer em diferentes situações.
#Rotinas pessoais: Criar lembretes, calcular gastos ou até gerar relatórios automáticos.