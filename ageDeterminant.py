
age = int(input("Type your age in figures: "))

if age <= 12:
    print ("Your age is {}, you are a KID" .format (age))
    
elif  age >= 13 and age <= 19:
    print ("Your age is {}, you are a TEENAGER" .format (age))
    
elif  age >= 20 and age <= 30:
    print ("Your age is {}, you are a YOUNG ADULT" .format (age))
    
elif  age >= 31 and age <= 64:
    print ("Your age is {}, you are an ADULT" .format (age))

