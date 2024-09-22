# a) Números ímpares
impares = [1, 3, 5, 7]
proximo_impar = impares[-1] + 2

# b) Potências de 2
potencias_de_2 = [2, 4, 8, 16, 32, 64]
proxima_potencia = potencias_de_2[-1] * 2

# c) Quadrados perfeitos
quadrados_perfeitos = [0, 1, 4, 9, 16, 25, 36]
proximo_quadrado = (len(quadrados_perfeitos)) ** 2

# d) Quadrados de números pares
quadrados_pares = [4, 16, 36, 64]
proximo_quadrado_par = (len(quadrados_pares) + 1) ** 2 * 4

# e) Sequência de Fibonacci
fibonacci = [1, 1, 2, 3, 5, 8]
proximo_fibonacci = fibonacci[-1] + fibonacci[-2]

# f) Sequência crescente com alguns pulos
sequencia = [2, 10, 12, 16, 17, 18, 19]
proximo_numero = sequencia[-1] + 1

# Resultados
print("a) Próximo número ímpar:", proximo_impar)  # 9
print("b) Próxima potência de 2:", proxima_potencia)  # 128
print("c) Próximo quadrado perfeito:", proximo_quadrado)  # 49
print("d) Próximo quadrado par:", proximo_quadrado_par)  # 100
print("e) Próximo número da sequência de Fibonacci:", proximo_fibonacci)  # 13
print("f) Próximo número da sequência:", proximo_numero)  # 20
