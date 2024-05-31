
# Python code to show the difference between creating a list and a tuple  
list_ = [4, 5, 7, 1, 7]  
tuple_ = (4, 1, 8, 3, 9)  
  
print("List is: ", list_)  
print("Tuple is: ", tuple_)  

# Code to print the data type of the data structure using the type() function  
print( type(list_) )  
print( type(tuple_))



print()
# Updating the element of list and tuple at a particular index  
  
# creating a list and a tuple  
list_ = ["Python", "Lists", "Tuples", "Differences"]  
tuple_ = ("Python", "Lists", "Tuples", "Differences")  
  
# modifying the last string in both data structures  
list_[3] = "Mutable"  
print( list_ )  
try:  
    tuple_[3] = "Immutable"  
    print( tuple_ )  
except TypeError:  
    print( "Tuples cannot be modified because they are immutable" )  


print()
# Code to show the difference in the size of a list and a tuple  
  
#creating a list and a tuple  
list_ = ["Python", "Lists", "Tuples", "Differences"]  
tuple_ = ("Python", "Lists", "Tuples", "Differences")  
# printing sizes   
print("Size of tuple: ", tuple_.__sizeof__())  
print("Size of list: ", list_.__sizeof__()) 


print()
print("MIXED LIST")

mixed_list = ['a', 1,'b',2,'c',3]
print(mixed_list)

print()
print("NESTED LIST")


nested_list = [1,2,3,[4,5,6],7,8]
print(nested_list)