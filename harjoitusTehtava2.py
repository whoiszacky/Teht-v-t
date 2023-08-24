def etsiToinen(a, b):
    ensin = a.find(b)
    toinen = a.find(b, ensin + 1)
    return toinen

# Pyydetään käyttäjältä merkkijonot a ja b
a = input("Syötä merkkijono a: ")
b = input("Syötä merkkijono b: ")

# Kutsutaan etsiToinen-funktiota ja näytetään toisen esiintymän indeksi
toinenIndeksi = etsiToinen(a, b)
print("Toisen esiintymän indeksi: ", toinenIndeksi)
