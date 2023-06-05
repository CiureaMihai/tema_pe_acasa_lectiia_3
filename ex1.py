"""1.	Creați 2 variabile x şi y, a căror valoare este citită de la tastatură.
Folosiți funcţia int() pentru a transforma valorile citite în numere întregi.
* Definiţi după aceasta variabila suma care va fi egală cu suma lui x şi y.
* Definiţi variabila **diff** care va fi egală cu x - y (diferenţa lui x şi y).
* Definiţi variabila **rest_impart** care va fi egală cu restul împărţirii lui x la y.
* Definiţi variabila **mult** care va fi egală cu x înmulţit cu y.
* Definiţi variabila **power3** care va fi egală cu x la puterea 3.
Afișați toate rezultatele
"""

x = int(input("Introduceți valoarea pentru x: "))
y = int(input("Introduceți valoarea pentru y: "))

suma = x + y
diff = x - y
rest_impart = x % y
mult = x * y
power3 = x ** 3

print("Suma lui x și y este:", suma)
print("Diferența lui x și y este:", diff)
print("Restul împărțirii lui x la y este:", rest_impart)
print("Înmulțirea lui x și y este:", mult)
print("x la puterea 3 este:", power3)