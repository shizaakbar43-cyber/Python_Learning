#Question 1: The Bill Splitter
bill = float(input("Enter total bill: "))
tip = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))
# perform operations
tot_tip = bill * tip / 100
tot_bill = bill + tot_tip
per_person = tot_bill / people
#Outputs
print("Total Tip:", tot_tip)
print("Total Bill:", tot_bill)
print("Each Person Pays:", per_person)


#Question 2: Password Strength Checker
password = input("Enter your password: ")
upper = False
lower = False
number = False
for ch in password:
    if ch.isupper():
        upper = True
    if ch.islower():
        lower = True
    if ch.isdigit():
        number = True
if len(password) < 6:
    print("Weak Password")
elif len(password) >= 8 :
    print("Strong Password")
else:
    print("Moderate Password")


#Question 3: The Guessing Game
secret = 42
attempts = 0
while attempts < 5:
    guess = int(input("Guess a number (1-100): "))
    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100")
        continue
    attempts += 1
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong Guess!")
else:
    print("Game Over! You lost.")


#Question 4: String Slicer & Manipulator
name = input("Enter your full name: ")
parts = name.split()
first = parts[0]
last = parts[-1]
print("Initials:", first[0] , ". " , last[0] , ".")
print("Uppercase:", name.upper())
print("Reversed:", name[::-1])

#Question 5: Global vs. Local Bank
bank_balance = 5000
def deposit(amount):
    global bank_balance
    bank_balance += amount
def withdraw(amount):
    global bank_balance
    if amount <= bank_balance:
        bank_balance -= amount
    else:
        print("Insufficient Balance")
deposit(1000)
print("After Deposit:", bank_balance)
withdraw(2000)
print("After Withdrawal:", bank_balance)


#Question 6: Unique Character Counter
sentence = input("Enter a long sentence: ")
characters = set(sentence.replace(" ", ""))
print("Unique Characters:", characters)
print("Total Unique Characters:", len(characters))

#Question 7: The Student Grading System
students = {
    "Ali": 85,
    "Ayesha": 92,
    "Ahmed": 75,
    "Sara": 60,
    "Usman": 88
}
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"
    print(name, "Marks:", marks, "Grade:", grade)



