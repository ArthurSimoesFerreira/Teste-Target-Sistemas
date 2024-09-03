def inverte_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Digite uma string para inverter: ")
print("String invertida:", inverte_string(string))
