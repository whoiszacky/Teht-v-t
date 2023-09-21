import random

lottorivi = input("Anna lottorivi (erottele numerot pilkulla): ").split(",")
lottorivi = [int(numero) for numero in lottorivi]
maara = int(input("Kuinka monta riviä arvotaan: "))

oikeat_numerot = []

for i in range(maara):
    arvottu_rivi = random.sample(range(1, 40), 7) # random.sample will return unique numbers
    oikeat_luvut = set(lottorivi) & set(arvottu_rivi)

    oikein = len(oikeat_luvut)
    oikeat_numerot.append(oikein)

    print(arvottu_rivi, "(", oikein, "oikein )")

print(oikeat_numerot.count(4), "kertaa neljä oikein!")
print(oikeat_numerot.count(5), "kertaa viisi oikein!")
print(oikeat_numerot.count(6), "kertaa kuusi oikein!")
print(oikeat_numerot.count(7), "kertaa seitsemän oikein!")
