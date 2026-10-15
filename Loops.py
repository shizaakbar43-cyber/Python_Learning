#Loops in Python
#For loop
for a in range(10):
    print(a)
n = int(input("Enter a number: "))
#For loop with range
for i in range(1, n + 1):
    print(i)
#For loop with break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)
#For loop with continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#For loop with pass statement
for i in range(3):
    pass
print("Done")

#While loop
b = 0
while b < 5:
    print(b)
    b += 1
j = int(input("Enter a starting number: "))
while j <= 10:
    print(j)
    j += 1
i = 1
#while loop of else statement
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")