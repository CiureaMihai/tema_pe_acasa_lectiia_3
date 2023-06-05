"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere
Note: Indiferent daca e majuscula sau minusucula litera
"""


sir = input("Introduceți un șir de caractere: ")

# Calculăm numărul total de litere în șir
numar_total_litere = len(sir)

# Inițializăm numărul de vocale și consoane cu 0
numar_vocale = 0
numar_consoane = 0

# Verificăm fiecare caracter în șir
for caracter in sir:
    caracter = caracter.lower()  # Convertim caracterul la literă mică pentru a face verificările indiferent de majusculă/minusculă
    if caracter.isalpha():  # Verificăm dacă caracterul este o literă
        if caracter in "aeiou":  # Verificăm dacă caracterul este o vocală
            numar_vocale += 1
        else:
            numar_consoane += 1

# Afișăm rezultatele
print("Numărul total de litere în șir: ", numar_total_litere)
print("Numărul de vocale în șir: ", numar_vocale)
print("Numărul de consoane în șir: ", numar_consoane)