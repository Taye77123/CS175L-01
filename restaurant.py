

vegetarian = False
vegan = False
gluten_free = False
response = input("is anyone in your party vegetarian?")  

if (response == 'yes'):
    vegetarian = True
response = input("is anyone in your party vegan?")
if (response == 'yes'):
    vegan = True
response = input("is anyone in your party gluten free?")
if (response == 'yes'):
    gluten_free = True
print("Here are your restaurant choices")

if ((vegetarian == False) and (vegan == False) and (gluten_free == False)):
    print("Joe's Gourmet Butgers")
    print("Corner Cafe")
    print("Chef's Kitchen")
elif ((vegan == False) and (gluten_free == False)):
    print("Mama's Fine Italian")
    print("Corner Cafe")
    print("Chef's Kitchen")
else:
    (vegan == False
    print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
