# Unohdin käyttää kahta eri funktio
'''def rotate(binary, steps, direction):
    if direction.lower() == "vasen":
        return binary[steps:] + binary[:steps]
    elif direction.lower() == "oikea":
        return binary[-steps:] + binary[:-steps]
    else:
        print("Virheellinen suunta!")
        return None

binary = input("Anna bitit: ")
steps = int(input("Anna pyöritysten lukumäärä: "))
direction = input("Anna pyörityksen suunta (vasen/oikea): ")

rotated_binary = rotate(binary, steps, direction)
if rotated_binary is not None:
    print("Pyöritettynä:", rotated_binary)'''


def rotate_left(binary, steps):
    return binary[steps:] + binary[:steps]

def rotate_right(binary, steps):
    return binary[-steps:] + binary[:-steps]

binary = input("Anna bitit: ")
steps = int(input("Anna pyöritysten lukumäärä: "))
direction = input("Anna pyörityksen suunta (vasen/oikea): ")

if direction.lower() == "vasen":
    rotated_binary = rotate_left(binary, steps)
elif direction.lower() == "oikea":
    rotated_binary = rotate_right(binary, steps)
else:
    print("Virheellinen suunta!")
    rotated_binary = None

if rotated_binary is not None:
    print("Pyöritettynä:", rotated_binary)
