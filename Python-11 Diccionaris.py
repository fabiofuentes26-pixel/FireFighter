"""
Exercici 1
"""
print("Exercici 1:\n")

alumne = {'nom': 'Anna', 'edat': 19, 'cicle': 'DAW'}

# nom alumne

print(alumne['nom'])

# canvi d'edat

alumne['edat'] = 20

# afegir clau ciutat

alumne['ciutat'] = 'Manresa'

# eliminar clau cicle

print("Eliminat:",alumne.pop('cicle'))

# diccionari final

print(alumne)
print()
"""
Exercici 2
"""
print("Exercici 2:\n")

preus = {'cafè': 1.20, 'te': 1.10, 'croissant': 1.50, 'entrepà': 3.50}

# demanar producte

producte = input(("Quin producte vols? "))
# a) comprovar la clau amb in

producte = producte.lower()
if producte in preus:
    print("El", producte, "val", preus[producte], "€")
else:
    print("No tenim aquest producte")
    
# b) Sense in, amb get

producte = producte.lower()
if preus.get(producte):
    print("El", producte, "val", preus[producte], "€")
else:
    print("No tenim aquest producte")
print()
"""    
Exercici 3
"""
print("Exercici 3:\n")

notes = {'Anna': 7.5, 'Marc': 4.2, 'Laia': 9.1, 'Pol': 5.0, 'Jan': 3.8}

# a) Recorrer el diccionari amb items()

for nom, nota in notes.items():
    print(f"{nom}: {nota}", "aprovat" if nota >= 5 else "suspès")
    
# b) calcular mitjana

mitjana = sum((notes.values()))
mitjana = mitjana / len(notes.values())
print("MItjana:",round(mitjana, 2))

# c) Nota més alta
max = nota
for nom, nota in notes.items():
    if nota >= max:
        max = nota
        millor = nom
print("Millor nota:",millor, ":", max)
print()
"""
Exercici 4
"""
print("Exercici 4:\n")

# a)
notes = {'Anna': 7.5, 'Marc': 4.2, 'Laia': 9.1, 'Pol': 5.0, 'Jan': 3.8}

aprovats = {nom: nota for nom, nota in notes.items() if nota >= 5}
print(aprovats)

# b)
paraules = ['python', 'dades', 'diccionari', 'set']

text = {paraula: len(paraula) for paraula in paraules}
print(text)

# c)
codis = {'BCN': 'Barcelona', 'GIR': 'Girona', 'LLE': 'Lleida', 'TGN': 'Tarragona'}

c = {ciutat:codi for codi,ciutat in codis.items()}
print(c)
print()
"""
Exercici 5
"""
print("Exercici 5:\n")

text = "el gat i el gos i el ratolí"

paraules = text.split()
diccionari = {}

for paraula in paraules:
    diccionari[paraula] = diccionari.get(paraula, 0) + 1

print(diccionari)

paraula_repetitiva = ""
maxim = 0

for paraula in diccionari:
    if diccionari[paraula] > maxim:
        maxim = diccionari[paraula]
        paraula_repetitiva = paraula

print(f"La paraula més repetida és {paraula_repetitiva} ({maxim} vegades)")
print()
"""
Exercici 6
"""
print("Exercici 6:\n")

inscripcions = [('Anna', 'M0485'), ('Marc', 'M0487'), ('Laia', 'M0485'), ('Anna', 'M0487'), ('Pol', 'M0485'), ('Jan', 'M0483')]

alumnes = {}

for alumne, modul in inscripcions:
    if modul not in alumnes:
        alumnes[modul] = []

    alumnes[modul].append(alumne)

for modul in sorted(alumnes):
    llista = sorted(alumnes[modul])

    print(f"{modul}: {len(llista)} alumne/s - {llista}")
