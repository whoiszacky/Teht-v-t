num = int(input("laita numero, jonka haluat tarkistaa, onko sen alkuluku vai ei \n"))

# tarkistaa jos num on suurempi kuin yksi

if num > 1:
	for i in range(2, int(num/2)+1):
		if (num % i) == 0:
			print(num, "ei ole alkuluku")
		break
	else:
		print(num, "on alkuluku")
