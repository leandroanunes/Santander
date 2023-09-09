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