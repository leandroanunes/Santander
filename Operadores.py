# Adição
print(1 + 5)

# Subtração
print(5 - 1)
# Multiplicação
print(10 * 2)

# Divisão
print(15 / 2)

# Divisão Inteira
print(10 // 2)

# Módulo (o resto da divisão)
print(10 % 3)

# Exponenciação
print(2 ** 3)

################### OPERADORES DE COMPARAÇÃO #########################
valor1 = 200
valor2 = 200

# Igual
print(valor1 == valor2)

# Diferente
print(valor1 != valor2)

# Maior que
print(valor1 > valor2)

# Menor que
print(valor1 < valor2)

# Menor ou igual a
print(valor1 <= valor2)

# Maior ou igual a
print(valor1 >= valor2)

################### OPERADORES DE ATRIBUIÇÃO #########################
saldo = 100  # Variavel principal


saldo += 100
# Realiza a conta direto na variavel 
# Funciona para qualquer tipo de conta 
print(saldo) 


################### OPERADORES LOGICOS #########################

dinheiro = 1000
saque = 250
limite = 500



resultado = dinheiro >= saque and saque <= limite
print(resultado)


################### OPERADORES DE ASSOCIAÇÃO #########################

curso = "Curso de Python"

frutas = ["pera", "melancia", "abacaxi"]

"Python" in curso
#>>> vai dar true

"maça" not in frutas
#>>> vai dar true, porque a maça realmente não está na lista