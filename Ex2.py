def contar_a(s):
    count = s.lower().count('a')
    if count > 0:
        return f"A letra 'a' ocorre {count} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."

# Exemplo de uso
string = input("Informe uma string: ")
print(contar_a(string))
