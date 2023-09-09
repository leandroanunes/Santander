valor = 100
limite = float(input("Informe o valor do Limite: "))

# Os códigos feitos em Python precisam ser escritos bem dentados e limpos, senão não funcionam
if valor <= limite:
    print("O valor é menor que o limite")
else:
    print("O valor é menor que o limite")

# else + if = elif

########################## FOR
texto = input("Escreva alguma palavra: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:  #só pra explicar esse .upper -- como as letras na variavel VOGAIS ta em maiusculo o upper é para acompanhar e identificar as letras
        print(letra, end="")  # Esse end="" é para não quebrar a linha no if, a quebra de linha ocorre só depois que acabar o for

print()         # Para adicionar uma quebra de linha

######################### while
opcao = -1
while opcao !=0:
    opcao = int(input("[1] vermelho \n[2] azul \n[3] amarelo \n[0] sair desse loop\n"))
    if opcao == 1:
        print("--> você escolheu a cor vermelho <--")
        print()
    elif opcao == 2:
        print("--> você escolheu a cor azul <--")
        print()
    elif opcao == 3:
        print("--> você escolheu a cor amarelo <--")
        print()
    elif opcao == 0:
        print()
    else:
        print("digite um numero valido!")
        print()
