#Objetivo: Calcular média de 3 notas.

#Declaração de variaveis.
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

#Processamento da média
media = (n1 + n2 + n3)/3

#Saída
print(f"Sua média foi {media}")

if media >= 6:
    print("Você foi aprovado")

else:
    print("Você foi reprovado seu abestado!!!")



