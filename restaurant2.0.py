#
#
#
keepGoing = False
vegetarian = False
vegan = False
gluten_free = False

response_1 = str(input("is anyone in your party vegetarian?"))
response_2 = str(input("is anyone in your party vegan?"))
response_3 = str(input("is anyone in your party gluten free?"))
                 
if (response_1 == 'yes'):
    vegetarian = True

if (response_2 == 'yes'):
    vegan = True

if (response_3 == 'yes'):
    gluten_free = True
                 
print("Here are your restaurant choices")

if (not vegetarian) and (not vegan) and (not gluten_free):
    print("Joe's Gourmet Butgers")
    print("Corner Cafe")
    print("Chef's Kitchen")
if (not vegan) and (not gluten_free):
    print("Mama's Fine Italian")
    print("Corner Cafe")
    print("Chef's Kitchen")
if not vegan:
    print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
    
response_4 = str(input("would you like to do another search?"))

keepGoing = True

if (response_4 == 'yes'):
     keepGoing = True
     
while keepGoing == True:
    response_1 = str(input("is anyone in your party vegetarian?"))
    response_2 = str(input("is anyone in your party vegan?"))
    response_3 = str(input("is anyone in your party gluten free?"))
    
    if keepGoing == False:
        break
