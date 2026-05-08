# ============================================================
# Python Final Project 2026
# Name: Zachuary Birdsong
# Date: 5/6/2026
# Project Title: Final Calculator
# Description: (Write 1-2 sentences explaining what your program does)This program will be able to calculate your final grade based on your list of grades given for a single class or give you a final gpa for your grades from your classes.
# ============================================================

playerName = input("What is your name?")

print("Welcome", playerName)
print("This program will calculate your final grade for a single class or all your classes.")


option = input("Do you want to calculate a single class grade or your GPA? Please input either 1 for SINGLE CLASS or 2 for GPA: ")
# This option will end up deciding how they want to calculate there classes.
if option == "1": 
    class1 = input("What class are your trying to calculate your final grade for?")
    userInput = input("Enter grades sperated by spaces: ")
    grades = [int(x) for x in userInput.split()]
    average = sum(grades) / len(grades)
    print("Your grade for class", class1, "is a", float(average), "%!")
elif option == "2":
    userInput2 = input("Enter the grade you have for each class, seperated by spaces: ")
    grades2 = [int(x) for x in userInput2.split()]
    average2 = sum(grades2) / len(grades2)
    gpa = (average2 / 100) * 4
    print("Your final grade", playerName, "is a", float(average2), "%, or a GPA of", float(gpa))
else:
    raise ValueError("Invalid statement, please input one of the following: 1 or 2.")


print("Thanks for using my program!")
