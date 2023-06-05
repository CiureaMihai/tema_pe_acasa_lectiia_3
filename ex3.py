
"""Declaraţi o variabilă price, de tip int, care va reţine preţul unui produs citit de la tastatură.
* Calculaţi cât va reprezenta 30% din preţul iniţial şi salvaţi valoarea în variabila reducere
*	Scădeţi din preţul iniţial valoarea reducerii, calculate la pasul precedent. Salvaţi valoarea în variabila preţ_final
* Creaţi o variabilă nouă pret_100_lei, şi salvaţi în această variabilă cât va fi preţul iniţial minus 100 lei
* Afişaţi la final ambele preturi.
"""

price = int(input("Introduceți prețul produsului: "))

reducere = price * 0.3
pret_final = price - reducere

pret_100_lei = price - 100

print("Prețul inițial:", price)
print("Reducerea (30%):", reducere)
print("Prețul final:", pret_final)
print("Prețul inițial minus 100 lei:", pret_100_lei)