"""
 Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""

sir = input("Introduceți un șir de caractere: ")
inceput = int(input("Introduceți poziția de început: "))
sfarsit = int(input("Introduceți poziția de sfârșit: "))

subsir = sir[inceput:sfarsit+1]
print("Subșirul extras este:", subsir)
