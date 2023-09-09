# TIPOS DE VARIAVEIS  

# Tipo Inteiro (int) - 123
# Ponto Flutuante ou Decimal (float) - 12.50
# Complexo (complex)
# String (str) "bla bla bla"
# Boolean (bool) true / false
# Listas (list) ['item1', 'item2', 'item3']
# Tuplas (tuple)
# Dicionários (dict) {nome: 'Leandro', email: 'leandro@gmail.com', idade: 21}


print("hello world!")

idade, nome, ano = (20, 'leandro', 2023)
print(f"meu nome é {nome}, tenho {idade} anos e estamos em {ano}")

ESTADOS_BRASILEIROS = ["SP", "RJ", "PA", "RS", "GO"]
print(ESTADOS_BRASILEIROS)

################### CONVERTENDO TIPOS #########################
# INTEIRO PARA FLOAT
# (FLOAT é uma variavel de numero que representa os numeros REAIS)

preco = 10
preco = float(preco)

print(preco)

# NUMERO PARA STRING

ano = 2020

print(str(ano))

# STRING PARA NUMERO
teste_string = "45"
print(int(teste_string))