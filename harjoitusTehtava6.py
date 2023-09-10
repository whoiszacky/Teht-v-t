def poistaDuplikaatit(lista):
    uniikit = []
    for alkio in lista:
        if alkio not in uniikit:
            uniikit.append(alkio)
    return uniikit

# Käytännön esimerkki:
lista = [1, 1, 2, 3, 1, 5, 2, 4, 3]
uniikit = poistaDuplikaatit(lista)
print(uniikit)


#hap fudud blase malaha wax function ah 
"""
Lista = [1, 1, 2, 3, 1, 5, 2, 4, 3]

uniqueList = []
for item in Lista:
    if Lista.count(item) > 1:
        while item in Lista:
            Lista.remove(item)
    uniqueList.append(item)

print(uniqueList)"""


