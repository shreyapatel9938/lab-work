# #Question 1:
num = int(input("Enter the value of number(Enter 0 to stop): "))

while(num != 0):
    print("You entered:",num)
    num = int(input("Enter the value of number(Enter 0 to stop): "))
print("Program terminated\n")

#===========================================
# #Question 2:
for i in range(1,11):
    print(i,"Square:",i*i)
print()

#===========================================
# #Question 3:
i = 2

while(i <= 50):
    print(i)
    i+=2
print()

#===========================================
# #Question 4:
for i in range(1,21,2):
    print(i)
print()

#===========================================
# #Question 5:
for i in range(5,51,5):
    print(i)
print()

#===========================================
# #Question 6:
for i in range(10,0,-1):
    print(i)
print()

#===========================================
# #Question 7:
for i in range(1,51):
    if(i % 2 == 0):
        if(i % 3 == 0):
            print(i,"is divisible by 2 and 3.")
        else:
            print(i,"is divisible by 2.")
    elif(i % 3 == 0):
        print(i,"is divisible by 3.")
    else:
        print(i,"is not divisible by 2 or 3.")