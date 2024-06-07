# Equality Operator Examples:
x1 = 5
y1 = 5
res = x1 == y1
print(res)

print()

string1 = "Hello"
string2 = "World"
result = string1 == string2  # This will result in False because the content of the two strings is different.

print(result)

print()

list1 = [1, 2, 3]
list2 = [1, 2, 3]
result1 = list1 == list2  # This will result in True because the content of the two lists is the same.
print(result1)

print()


# Inequality Operator Examples:
string1 = "Hello"
string2 = "Hello"
result2 = string1 != string2  # This will result in False because the content of the two strings is the same.

print(result2)


print()
# Examples of Less Than Operator:
# Checking if one number is less than another:
x = 5
y = 10
result = x < y  # This will result in True because 5 is less than 10.
print(result)


print()
# Comparing strings lexicographically:
string1 = "apple"
string2 = "banana"
result = string1 < string2  # This will result in True because "apple" comes be
print(result)


print()

x = 10
y = 5
result = x > y  # This will result in True because 10 is greater than 5.
print(result)


print()

# Comparing strings lexicographically:
string1 = "banana"
string2 = "apple"
result = string1 > string2  # This will result in True 
# because "banana" comes after "apple" in lexicographic order.
print(result)



print()
# Less Than or Equal To (<=) Operator in Python
x = 5
y = 10
result = x <= y  # This will result in True because 5 is less than 10.
# Comparing strings lexicographically:
string1 = "apple"
string2 = "banana"
result = string1 <= string2  # This will result in True because "apple" comes 
# before "banana" in lexicographic order, and it's also equal in length.
print(result)

print()

x = 10
y = 5
result = x >= y  # This will result in True because 10 is greater than 5.
# Comparing strings lexicographically:
string1 = "banana"
string2 = "apple"
result = string1 >= string2
print(result)





print()
print("Comparison Operators using If_Else")

x = 1
y = 2

# Using the eqaul to comparison operator
if x == y:
  print('Line 1: x is equal to y')
else:
  print('Line 1: x is not equal to y')


# Using the not eqaul to comparison operator
if x != y:
  print('Line 2: x is not equal to y')
else:
  print('Line 2: x is equxl to y')


# Using the greater than comparison operator
if x > y:
  print('Line 3: x is greater than y')
else:
  print('Line 3: x is not greater thab y')


# Using the less than comparison operator
if x < y:
  print('Line 4: x is less than y')
else:
  print('Line 4: x is not less than y')


# Using the greater than or equal to  comparison operator
if x >= y:
  print('Line 5: x is greater than or equal to y')
else:
  print('Line 5: x is not greater than or equal to y')

  
# Using the less than or equal to  comparison operator
if x <= y:
  print('Line 6: x is lesser than or equal to y')
else:
  print('Line 6: x is not lesser than or equal to y')