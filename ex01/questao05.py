def inverter_string(original):
    tamanho = len(original)
    invertida = ""

    for i in range(tamanho - 1, -1, -1):
        invertida += original[i]

    return invertida


string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)

print(f"A string invertida é: {string_invertida}")
