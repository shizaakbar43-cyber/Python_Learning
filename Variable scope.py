# Two types of variable scope in Python:
# 1. Local scope: A variable defined inside a function is said to have a local scope. It can only be accessed within that function.
# 2. Global scope: A variable defined outside of all functions is said to have a global scope. It can be accessed from anywhere in the program.
#Local scope
def local_var():
    x = 10 
    print("Local variable x:", x)

local_var()

#Global scope
y = 20  
def Global_var():
    print("Global variable y:", y)
Global_var()
print("Outside function:", y) 
