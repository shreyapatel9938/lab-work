# =>. ef-else statement:
# 1. Write a program to accept two integers and check whether they are equal or not.
num_1 = int(input("Enter the value of number 1: "))
num_2 = int(input("Enter the value of number 2: "))

if(num_1 == num_2):
    print("Numbers are equal.")
else:
    print("Numbers are not equal.")

#=========================================================
# 2. Write a program to check whether a given number is even or odd.
num = int(input("Enter the a number: "))

if(num % 2 == 0):
    print("Number is even.")
else:
    print("Number is odd.")

#=========================================================
# 3. Write a program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.
age = int(input("Enter your age: "))

if(age >= 18):
    print("Candidate is eligible to vote.")
else:
    print("Candidate is not eligible to vote.")

#=========================================================
# #4. Write a program to ,
#     read the value of an integer m    (user input)
#         and display the value of n.

#         n is 1 when m is larger than 0 and -1 when m is less than 0.
m = int(input("Enter the value of m: "))
n = 0
if(m > 0):
    n = 1
elif(m == 0):
    n = 0
else:
    n = -1
print("The value of n =",n) 
#=========================================================
# =>. ladder if-else statement:
# 1. Write a  program to read temperature in centigrade and display a suitable message according to the temperature state below:
# Temp < 0 then Freezing weather
# Temp 0-10 then Very Cold weather
# Temp 10-20 then Cold weather
# Temp 20-30 then Normal in Temp
# Temp 30-40 then Its Hot
# Temp >=40 then Its Very Hot
temp = int(input("Enter temperature in centigrade: "))

if(temp < 0):
    print("Freezing weather")
elif(temp <= 10):
    print("Very Cold weather")
elif(temp <= 20):
    print(" Cold weather")
elif(temp <= 30):
    print("Normal in Temp")
elif(temp < 40):
    print("Its Hot")
else:
    print(" Its Very Hot")

#=========================================================
#2. Write a  program to check whether a triangle is Equilateral, Isosceles or Scalene.
side_1 = int(input("Enter the value of first side: "))
side_2 = int(input("Enter the value of second side: "))
side_3 = int(input("Enter the value of third side: "))
if(side_1 <= 0 or side_2 <= 0 or side_3 <= 0):
    print("Invalid sides. Sides must be positive.")
elif(side_1 + side_2 <= side_3 or side_2 + side_3 <= side_1 or side_1 + side_3 <= side_2):
    print("These sides cannot form a triangle.")
elif(side_1 == side_2 == side_3):
    print("This is an Equilateral triangle.")
elif(side_1 == side_2 or side_2 == side_3 or side_1 == side_3):
    print("This is an Isosceles triangle.")
else:
    print("This is a Scalene triangle.")

#=========================================================
# 3. Write a program to check whether a triangle can be formed with the given values for the angles.
angle_1 = int(input("Enter the value of first angle: "))
angle_2 = int(input("Enter the value of second angle: "))
angle_3 = int(input("Enter the value of third angle: "))

if(angle_1 <= 0 or angle_2 <= 0 or angle_3 <= 0):
    print("Angles must be positive.")
elif(angle_1 >= 180 or angle_2 >= 180 or angle_3 >= 180):
    print("Triangle is not possible")
elif (angle_1 + angle_2 + angle_3 == 180):
    print("Triangle is possible.")
elif(angle_1 + angle_2 + angle_3 > 180):
    print("Sum of angles is greater than 180 so triangle cannot be possible.")
else:
    print("Sum of angles is less than 180 so triangle cannot be possible.")

#=========================================================
# =>. Nested if else statement:
# 1. Write a program to find whether a given year is a leap year or not.
year = int(input("Enter the year: "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(year,"is leap year.")
        else:
            print(year,"is not leap year.")
    else:
       print(year,"is leap year.")
else:
    print(year,"is not leap year.")
    
#=========================================================