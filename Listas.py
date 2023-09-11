# Uma lista é feita usando VAR ["bla", "bla2", 123, 32, etc.]
# Exemplo 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 45, 99]

# Vamos criar um laço de repetição usando a lista

for pares in numeros:
    if pares %2 == 0:
        print(pares,"| ", end="")

# Esse laço de repetição vai separar os numeros pares 
# Mas também pode ser escrito assim:

impares =[numeros for numeros in numeros if numeros %2 == 1]
print(impares)

# Deste segundo jeito fica mais facil de deixar a lista compreensivel e bonita!

############### MATRIZ
matriz = (
    (1, "a", 2),
    (4, "d", 9),
    (15, "he", 8),
)

print("O valor escolhido é: ", matriz[0][2]) # O primeiro [] é a coluna, e o segundo [] é a linha

############# SET
# Set é para organizar a lista caso tenha algo repetido

cores = set(("azul", "vermelho", "azul", "preto", ))
print(cores)

SET_com_numeros = set([1, 2, 3, 4, 1])
print(SET_com_numeros)

############# INTERSECTION, DIFFERENCE & SYMMETRIC_DIFFERENCE
# INTERSECTION: Isso compara 2 conjuntos e acha o que é igual
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {5, 6, 7, 8, 9}
conjunto_c = {1, 2}

print(conjunto_a.intersection(conjunto_b))

# DIFFERENCE: ele vai pegar a diferença dos conjuntos (o que não tem em um conjunto comparado ao outro)
print(conjunto_b.difference(conjunto_a))

# SIMETRIC_DIFFERENCE: ele vai pegar a diferença dos conjuntos (o que é diferente em ambos os conjuntos)
print(conjunto_b.symmetric_difference(conjunto_a))

# ISSUBSET: Confere se todos os elementos estão dentro de outro conjunto
# TRUE or FALSE
print(conjunto_c.issubset(conjunto_a))

# ISDISJOINT: Confere se todos os elementos NÃO estão dentro de outro conjunto
# TRUE or FALSE
print(conjunto_c.isdisjoint(conjunto_b))


################### ADD
# Adiciona um elemento
lista_exemplo = {1,2, 4, 6, 7, 8}

lista_exemplo.add(24)
print(lista_exemplo)

################### DISCARD
# Descarta um elemento
lista_exemplo.discard(24)
print(lista_exemplo)