"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""

propozitie = input("Introduceți o propoziție: ")

caractere_punctuatie = [".", ",", "!", "?", ";", ":", "(", ")", "[", "]", "{", "}", "'", "\""]

propozitie_fara_punctuatie = ""
for caracter in propozitie:
    if caracter not in caractere_punctuatie:
        propozitie_fara_punctuatie += caracter

print("Propoziția fără punctuație: ", propozitie_fara_punctuatie)