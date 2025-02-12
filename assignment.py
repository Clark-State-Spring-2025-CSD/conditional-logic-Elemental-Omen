#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

print("welcome to the season finder 3000!")
month = int(input("What month is it? (1-12): "))
if month == 1:
    print("The month is January and the current season is Winter.")
elif month == 2:
    print("The month is February and the current season is Winter.")
elif month == 3:
    print("The month is March and the current season is Spring.")
elif month == 4:
    print("The month is April and the current season is Spring.")
elif month == 5:
    print("The month is May and the current season is Spring.")
elif month == 6:
    print("The month is June and the current season is Summer.")
elif month == 7:
    print("The month is July and the current season is Summer.")
elif month == 8:
    print("The month is August and the current season is Summer.")
elif month == 9:
    print("The month is September and the current season is Fall.")
elif month == 10:
    print("The month is October and the current season is Fall.")
elif month == 11:
    print("The month is November and the current season is Fall.")
elif month == 12:
    print("The month is December and the current season is Winter.")
else:
    print("We only got 12 months bud. You thought you were cleaver huh? This time put in a number between 1 and 12.")