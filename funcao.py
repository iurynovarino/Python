#Função é um bloco de código indentificado por um nome, podendo receber ou não parametros. Tem um conjunto de entradas e saídas.

#def exibir_mensagem(): #Função sem parametros de entrada
#   print("Olá mundo!")

#def exibir_mensagem_2(nome):
#    print(f"Seja bem vindo {nome}!")

#exibir_mensagem()
#exibir_mensagem_2(nome="guilherme")

#Para retorna um valor será necessário usar a palavra "return". Por padrão o python retorna #"none"

#def calcular_total(numeros):
#    return sum(numeros)

#def retorna_antecessor_e_sucessor(numero):
#    antecessor = numero - 1
#    sucessor = numero + 1

#   return antecessor, sucessor

#print(calcular_total([10, 20, 34]))
#print(retorna_antecessor_e_sucessor(10))

'''
As funções podem trabalhar com variaveis globais ou locais. As globais são definidas fora do escopo da função e a local é definida dentro da função. Para utilizar uma variável global é necessário usar a palavra reservada "global" em seguida o nome da variável.
'''

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

