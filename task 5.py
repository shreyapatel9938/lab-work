#Question 1:
num1 = float(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))

if num1 > num2:
    if num1 > num3:
        print("Number 1 is greater.")
    elif num3 > num1:
        print("Number 3 is greater.")
    else:
        print("Number 1 and Number 3 are same and greater.")

elif num2 > num1:
    if num2 > num3:
        print("Number 2 is greater.")
    elif num3 > num2:
        print("Number 3 is greater.")
    else:
        print("Number 2 and Number 3 are same and greater.")

else:
    if num1 > num3:
        print("Number 1 and Number 2 are same and greater.")
    elif num3 > num1:
        print("Number 3 is greater.")
    else:
        print("All are equal.")

#======================================================

#Question 2:
num1 = float(input("\nEnter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
num3 = int(input("Enter the value of num3 :"))


if(num1 < num2):
    if(num1 < num3):
        print("number 1 is smaller.")
    elif(num3 < num1):
        print("number 3 is smaller.")
    else:
        print("number 1 and number 3 are same and smaller.")        

elif(num2 < num1): 
    if(num2 < num3):
        print("number 2 is smaller.")  
    elif(num3 < num2):
        print("number 3 is smaller.") 
    else:
        print("number 2 and number 3 are same and smaller.") 
else:
    if(num1 < num3):
        print("number 1 and number 2 are same and smaller.")  
    elif(num3 < num1):
        print("number 3 is smaller.")
    else:
        print("All are equal.")

#======================================================
                   
#Question 4:

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator(+, - *, /): ")

match op:
    case "+" :
        print("Result:",a+b)
    case "-":
        print("Result:",a-b)
    case "*":
        print("Result:",a*b)
    case "/":
        if(b != 0):
            print("Result:",a/b)
        else:
            print("Cann't divisible by zero.")
    case _:
        print("Invalid operator.")
#======================================================
                   
#Question 5:
print("\nPress 1 to order a Sandwich")
print("Press 2 to order a Pizza")
print("Press 3 to order a Burger")

choice_1 = int(input("\nEnter your choice: "))

match choice_1:
    case 1: 
        print("\nSandwich Menu")
        print("1. Veg Sandwich")
        print("2. Cheese Sandwich")
        print("3. Corn Cheese Sandwich")

        choice_2 = int(input("\nChoose Sandwich: "))

        match choice_2:
            case 1: 
                print("You ordered Veg Sandwich.")
            case 2:
                print("You ordered Cheese Sandwich.")
            case 3:
                print("You ordered Corn Cheese Sandwich.")
            case _:
                print("Invalid choice! Please enter a valid choice.")
            
    case 2:
        print("\nPizza Menu")
        print("1. Margherita Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Veggie Paradise Pizza")

        choice_2 = int(input("\nChoose Pizza: "))
        
        match choice_2:
            case 1: 
                print("You ordered Margherita Pizza.")
            case 2:
                print("You ordered Cheese Burst Pizza.")
            case 3:
                print("You ordered Veggie Paradise Pizza.")
            case _:
                print("Invalid choice! Please enter a valid choice.")
    case 3:
        print("\nBurger Menu")
        print("1. Veg Burger")
        print("2. Bacon BBQ Burger")
        print("3. Classic Cheese Burger")

        choice_2 = int(input("\nChoose Burger: "))
                
        match choice_2:
            case 1: 
                print("You ordered Veg Burger.")
            case 2:
                print("You ordered Bacon BBQ Burger.")
            case 3:
                print("You ordered Classic Cheese Burger.")
            case _:
                print("Invalid choice! Please enter a valid choice.")

    case _:
        print("Invalid choice! Please enter a valid choice.")

#======================================================
                   
#Question 6:
print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")


choice_1 = int(input("\nSelect your language: "))
match choice_1:
    case 1:
        print("English Service")
        print("1. Recharge")
        print("2. Data Balance")
        print("3. Customer Care")

        choice_2 = int(input("\nSelect Service: "))
        match choice_2:
            case 1:
                print("English: Recharge Service selected.")
            case 2:
                print("English: Data Balance Service selected.")
            case 3:
                print("English: Connecting to Customer Care.")
            case _:
                print("Invalid choice! Please enter valid choice.")

    case 2:
        print("Hindi Service")
        print("1. Recharge")
        print("2. Data Balance")
        print("3. Customer Care")
        
        choice_2 = int(input("Select Service: "))
        match choice_2:
            case 1:
                print("Hindi: Recharge Service selected.")
            case 2:
                print("Hindi: Data Balance Service selected.")
            case 3:
                print("Hindi: Connecting to Customer Care.")
            case _:
                print("Invalid choice! Please enter valid choice.")

    case 3:
        print("Gujarati Service")
        print("1. Recharge")
        print("2. Data Balance")
        print("3. Customer Care")
        
        choice_2 = int(input("Select Service: "))
        match choice_2:
            case 1:
                print("Gujarati: Recharge Service selected.")
            case 2:
                print("Gujarati: Data Balance Service selected.")
            case 3:
                print("Gujarati: Connecting to Customer Care.")
            case _:
                print("Invalid choice! Please enter valid choice.")

    case _:
        print("Invalid choice! Please enter valid choice.")