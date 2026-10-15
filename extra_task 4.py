num_1 = int(input("Enter the value of number 1: "))
num_2 = int(input("Enter the value of number 2: "))
num_3 = int(input("Enter the value of number 3: "))
num_4 = int(input("Enter the value of number 4: "))

if (num_1 > num_2 and num_1 > num_3 and num_1 > num_4):
    print("Number 1 is greatest.")

elif(num_2 > num_1 and num_2 > num_3 and num_2 > num_4): 
    print("Number 2 is greatest.")

elif(num_3 > num_1 and num_3 > num_2 and num_3 > num_4):
    print("Number 3 is greatest.")

elif(num_4 > num_1 and num_4 > num_2 and num_4 > num_3):
    print("Number 4 is greatest.")

elif(num_1 == num_2 and num_1 > num_3 and num_1 > num_4):
    print("Number 1 and Number 2 are equal and greatest.")

elif(num_1 == num_3 and num_1 > num_2 and num_1 > num_4):
    print("Number 1 and Number 3 are equal and greatest.")   

elif(num_1 == num_4 and num_1 > num_2 and num_1 > num_3):
    print("Number 1 and Number 4 are equal and greatest.") 

elif(num_2 == num_3 and num_2 > num_1 and num_2 > num_4):
    print("Number 2 and Number 3 are equal and greatest.")

elif(num_2 == num_4 and num_2 > num_1 and num_2 > num_3 ):
    print("Number 2 and Number 4 are equal and greatest.")

elif(num_3 == num_4 and num_3 > num_1 and num_3 > num_2):
    print("Number 3 and Number 4 are equal and greatest.")

elif(num_1 == num_2 == num_3 and num_1 >num_4):
    print("Number 1, Number 2 and Number 3 are equal and greatest.")

elif(num_1 == num_2 == num_4 and num_1 >num_3):
    print("Number 1, Number 2 and Number 4 are equal and greatest.")

elif(num_1 == num_3 == num_4 and num_1 >num_2):
    print("Number 1, Number 3 and Number 4 are equal and greatest.")

elif(num_2 == num_3 == num_4 and num_2 >num_1):
    print("Number 2, Number 3 and Number 4 are equal and greatest.")
    
elif(num_1 == num_2 == num_3 == num_4):
    print("All four numbers are equal.")