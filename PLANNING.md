# 📝 Project Planning Worksheet

**Name:** Zachuary Birdsong  
**Date:** 5/6/2026  
**Project Title:** Final Grade Calculator

---

## Step 1 — What will your program do?

*Write 2–3 sentences describing your project. What happens when the user runs it? What will they see or do?*

> This will be a final grade calculator taking all the grades that you input and averaging them together. This will give you a final grade and maybe even a possible final GPA. All they have to do is input their class and grades.

---

## Step 2 — What will you ask the user?

*List every `input()` question you plan to use.*

1. What is your name?
2. Do you want to calculate a single class grade or your GPA? Please input either 1 for SINGLE CLASS or 2 for GPA: 
3. What class are your trying to calculate your final grade for?
4. Enter grades sperated by spaces:
5. Enter the grade you have for each class, seperated by spaces:

---

## Step 3 — What variables do you need?

*List the variable names you plan to use and what each one stores.*

| Variable Name | What It Stores | Data Type |
|---------------|---------------|-----------|
| planerName | the username | string |
| option | 1 or 2 | string |
| class1 | What the class is | string |
| userInput | list of grades for class1 | string |
| average | an average based on your grades | integer |
| grades | the same list as userInput but as integers | integers |
| userInput2 | list of grades | string |
| grade2 | the same list as userInput2 but as integers | integers |
| average2 | an average based on your grades2 | integer |
| gpa | a single number between 0-4 | integer |
---

## Step 4 — What decisions will your program make?

*Describe each `if/elif/else` check your program will use.*

if option == "1": 
    class1 = input("What class are your trying to calculate your final grade for?")
    userInput = input("Enter grades sperated by spaces: ")
    grades = [int(x) for x in userInput.split()]
    average = sum(grades) / len(grades)
    print("Your grade for class", class1, "is a", average, "%!")
elif option == "2":
    userInput2 = input("Enter the grade you have for each class, seperated by spaces: ")
    grades2 = [int(x) for x in userInput2.split()]
    average2 = sum(grades2) / len(grades2)
    gpa = (average2 / 100) * 4
    print("Your final grade", playerName, "is a", average2, "%, or a GPA of", gpa)
else:
    raise ValueError("Invalid statement, please input one of the following: 1 or 2.")

--- 

## Step 5 — What will the output look like?

*Write out what a sample run of your program might look like. Pretend you are the user.*

```
Program output here...What is your name?
User types: Bob
Program responds: Welcome Bob
This program will calculate your final grade for a single class or all your classes.
Do you want to calculate a single class grade or your GPA? Please input either 1 for SINGLE CLASS or 2 for GPA:
User types: 2
What class are your trying to calculate your final grade for?
User types: math
Enter grades sperated by spaces:
User types: 80 90 99 97 100 78
```
