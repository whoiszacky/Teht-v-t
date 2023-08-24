import math 

 

x1= float(input("Enter a number x1: ")) 

y1= float(input("Enter a number y1: ")) 

x2= float(input("Enter a number x2: ")) 

y2= float(input("Enter a number y2: ")) 

#Käytin tätä muuttujaa yksinkertaistamaan matematiikkaa 

potensi= math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) 

# tää muttaja holds the square root eli neliöjuuri 

neliöjuuri = math.sqrt(potensi) 

print(neliöjuuri) 
