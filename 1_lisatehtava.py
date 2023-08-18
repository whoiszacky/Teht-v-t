# Toisen asteen yhtälön

import math 
a = int(input("give A a value" )) 
b = int(input("give B a value" )) 
c = int(input("give C a value" )) 


# Jos juurrettava on negatiivinen eli b2−4ac<0, ei yhtälöllä ole ratkaisuja. 
d = (b**2) - (4*a*c) 

# ratkaisu Toisen asteen yhtälön 
rakaisu1 = (-b-math.sqrt(d))/(2*a) 
ratkaisu2 = (-b+math.sqrt(d))/(2*a) 

print("juuret ovat", rakaisu1, ratkaisu2) 
