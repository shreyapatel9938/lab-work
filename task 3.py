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

#====================================================
#question 2:

num = float(input("\nEnter a floating point number: "))
int_num = int(num)
print("Original floating point number: ",num)
print("Converted integer number: ",int_num)
print("Difference: int() removes decimal part.")

#====================================================
#question 3:

value = input("\nEnter True or False: ")
boolean_value = value == "True"

integer_value = int(boolean_value)
string_value = str(boolean_value)

print("Boolean value: ",boolean_value)
print("Integer value: ",integer_value)
print("String value: ",string_value)

#====================================================
#question 4:
