#Functions
def first_func():
    print("This is my first function")

first_func()
#Function with parameters
def add_no(a, b):
    return a + b

result = add_no(5, 3)
print("Sum: ", result)
#Function with default parameters
def greet(name="Shiza"):
    print("Hello, " , name)

greet()
#Function inside a function
def outer_func():
    print("This is the outer function")
    def inner_func():
        print("This is the inner function")
    inner_func()

outer_func()