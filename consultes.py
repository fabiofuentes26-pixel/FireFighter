from ciutats import ciutats

codi = input("Introdueix un codi postal: ")

trobat = False

for ciutat, dades in ciutats.items():
    if dades["codi_postal"] == codi:
        print("La ciutat és:", ciutat)
        trobat = True

if not trobat:
    print("No s'ha trobat cap ciutat amb aquest codi postal.")
    
print("Consulta de codis postals - Versió Beta")
print("Consulta de codis postals - Versió Master")
