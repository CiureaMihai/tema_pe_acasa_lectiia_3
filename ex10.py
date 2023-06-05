
"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""

propozitie = input("Introduceți propoziția: ")
sir_tinta = input("Introduceți subșirul de caractere țintă: ")
sir_inlocuire = input("Introduceți subșirul de caractere de înlocuire: ")

propozitie_modificata = propozitie.replace(sir_tinta, sir_inlocuire)
print("Propoziția modificată:", propozitie_modificata)