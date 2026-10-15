#Data structures: list, tuple, set, dictionary
#list
first_list = [1, 2, 3, 4, 5,6,7]
print("First list:", first_list)
my_list = input("Enter a list : ").split()
#use For loop in it
my_list = [int(a) for a in my_list]
print("My list:", my_list)

#tuple
my_tuple = (1, 2, 3, 4, 5)
print("My tuple:", my_tuple)
first_tuple = input("Enter a tuple : ").split()
first_tuple=tuple(int(a) for a in first_tuple)
print("First tuple:", first_tuple)

#Set
first_set = {1, 2, 3, 4, 5}
print("My set:", first_set)
print("Enter a set : ")
my_set = input().split()
my_set = {int(a) for a in my_set}
print("My set:", my_set)

#Dictionary
my_dict = {"name": "Shiza", "age": 20, "city": "Sheikhupura"}
print("My dictionary:", my_dict)