#creat the list of food that choose for you to eat.
dinner_list = ["pizze","cereal"," saled","fish","pasta"]
drink_list =  ["organ juice", "coke", "water","apple juice"]
dessart_list = ["cupcake", "ice cream","pie"]
#Generates a random integer.
i = randint(0, len(dinner_list)-1)
d = randint(0,len(drink_list)-1)
e = randint(0,len(dessart_list)-1)
#
dinner += dinner_list[i] + "" + drink_list[d] + "" + dessart_list[e]
#intitialize the dinner.
dinner = ""

print ("Your dinner is" + dinner)
