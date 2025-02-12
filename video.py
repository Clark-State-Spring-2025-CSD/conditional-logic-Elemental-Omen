#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $12 price tag.

print("Welcome to the Menu Ordering System")

customerAge=int(input("What is the age of the customer?"))

Price = 0

if customerAge <=12:
    Price = 8
elif customerAge <62:
    Price = 9
else:
    Price = 12

print(f"The price for the customer is ${Price}.")

drinkYesNo = input("Add a drink? (y/n)")

if drinkYesNo == "y":
    smallLarge = input("Small or Large? (s/l)")
    if smallLarge=="l":
        Price += 2
    else:
        Price += 1
        
print(f"The total price for the customer is ${Price}.")
