#Conditional statment in python such as if, elif and else
#if statement
n = int(input("Enter a number: "))
if n > 0:
     print("The number is positive")
 #For if-else statement
n = int(input("Enter a number: "))
if n%2 == 0:
     print("The number is Even")
else:
     print("The number is Odd")
#For if-elif-else statement
n = int(input("Enter a number: "))
if n > 0:
     print("The number is positive")
elif n < 0:
     print("The number is negative")
else:
     print("The number is zero")
#For if-elif-else statement
marks = int(input("Enter marks: "))
if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 40:
    print("Grade: E")
else:
    print("Grade: F")
#For nested if statement
marks = int(input("Enter marks: "))
if marks >= 80:
    if marks >= 90:
            print("Excellent")
    else:
            print("Very Good")
elif marks >= 70:
        print("Good")
else:
        print("Needs Improvement")

