"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""


def este_palindrom(sir):
    sir = sir.lower()  # Convertim toate caracterele la litere mici pentru a evita diferențele de litere mari și mici
    sir = sir.replace(" ", "")  # Eliminăm toate spațiile din șir

    invers = ""
    for caracter in sir:
        invers = caracter + invers

    if sir == invers:
        return True
    else:
        return False

# Testăm funcția
s = input("Introduceți un șir de caractere: ")
if este_palindrom(s):
    print("Este un palindrom.")
else:
    print("Nu este un palindrom.")