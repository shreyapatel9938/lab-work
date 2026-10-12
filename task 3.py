#question 1:
value = input("Enter a value: ")

integer_value = int(value)
float_value = float(value)
boolean_value = bool(value)

print("Intger value: ",integer_value)
print("Type: ",type(integer_value))

print("Float value: ",float_value)
print("Type: ",type(float_value))

print("Boolean value: ",boolean_value)
print("Type: ",type(boolean_value))

print("===================================================")
#question 2:

num = float(input("\nEnter a floating point number: "))
int_num = int(num)
print("Original floating point number: ",num)
print("Converted integer number: ",int_num)
print("Difference: int() removes decimal part.")

print("===================================================")
#question 3:

value = input("\nEnter True or False: ")
boolean_value = value == "True"

integer_value = int(boolean_value)
string_value = str(boolean_value)

print("Boolean value: ",boolean_value)
print("Integer value: ",integer_value)
print("String value: ",string_value)

print("===================================================")
# question 4:

integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True
list_value = [10, 20, 30]
tuple_value = (10, 20, 30)
dict_value = {"name":"Alice", "year": 25}

print("value:",integer_value, "\nType:",type(integer_value), "\nMemory address:",id(integer_value))
print()
print("value:",float_value, "\nType:",type(float_value), "\nMemory address:",id(float_value))
print()
print("value:",string_value, "\nType:",type(string_value), "\nMemory address:",id(string_value))
print()
print("value:",boolean_value, "\nType:",type(boolean_value), "\nMemory address:",id(boolean_value))
print()
print("value:",list_value, "\nType:",type(list_value), "\nMemory address:",id(list_value))
print()
print("value:",tuple_value, "\nType:",type(tuple_value), "\nMemory address:",id(tuple_value))
print()
print("value:",dict_value, "\nType:",type(dict_value), "\nMemory address:",id(dict_value))
print()

print("===================================================")
#question 5:

a = 100
b = 100
print("\nBefore Modification:")
print("a =",a ,"\nMemory address:",id(a))
print("b =",b ,"\nMemory address:",id(b))
print("\nAre memory address same?",id(a) == id(b))

a = 200
print("\nAfter modifying a:")
print("a =",a ,"\nMemory address:",id(a))
print("b =",b ,"\nMemory address:",id(b))
print("Are memory address same?",id(a) == id(b))  

print("===================================================")
