#Question 1:
num = int(input("Enter the value of number: "))

if num % 2 ==0:
    print("Number is even.")
else:
    print("Number is odd.")

#===================================================
#Question 2:
age = int(input("\nEnter your age: "))
if age < 0:
    print("Please enter valid age.")
else:
    if age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    elif age >= 60:
        print("Senior")

#===================================================
#Question 3:
num1 = float(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))

if num1 > num2:
    if num1 > num3:
        print("Number 1 is largest.")
    elif num3 > num1:
        print("Number 3 is largest.")
    else:
        print("Number 1 and Number 3 are same and largest.")

elif num2 > num1:
    if num2 > num3:
        print("Number 2 is largest.")
    elif num3 > num2:
        print("Number 3 is largest.")
    else:
        print("Number 2 and Number 3 are same and largest.")

else:
    if num1 > num3:
        print("Number 1 and Number 2 are same and largest.")
    elif num3 > num1:
        print("Number 3 is largest.")
    else:
        print("All are equal.")
#===================================================
#Question 4:
num = int(input("\nEnter the value of number: "))

if num > 0:
    print("Number is positive.")
elif num > 0:
    print("Number is Negative.")
else:
    print("Number is neutral.")