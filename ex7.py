
"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).
 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""

sir = input("Introduceți un șir de caractere: ")
caracter_cautat = input("Introduceți caracterul căutat: ")

# Convertim ambele caractere la litere mici pentru a face verificările indiferent de majusculă/minusculă
sir = sir.lower()
caracter_cautat = caracter_cautat.lower()

# Inițializăm numărul de apariții cu 0
numar_aparitii = 0

# Parcurgem fiecare caracter din șir și numărăm aparițiile
for caracter in sir:
    if caracter == caracter_cautat:
        numar_aparitii += 1

# Afișăm rezultatul
print("Numărul de apariții ale caracterului", caracter_cautat, "în șir:", numar_aparitii)