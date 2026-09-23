age = int(input("Please enter your age: "))

if age <= 0:
    input("invalid age entered")
elif age <5:   #Children under 5
    print("Your ticket is free!") 
elif age >=5 <= 12:  #Children aged 5 to 12
    print("Your ticket price is $8.")
elif age >=13 <=64:  #Teens & Adults aged 13 tp 64
    print("Your ticket price is $15.")
else:  #Seniors aged 65 and above:
    print("your ticket price is $10")
