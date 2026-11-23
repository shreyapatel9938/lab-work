# Question 1:

# marks =[50,79,48,86,99]
# print("Original:",marks)
# print("Total studenet:",len(marks))
# print("Highest marks:",max(marks))
# print("Sorted marks:",sorted(marks))
# print("Data type:",type(marks))

# =======================================================
# Question 2:

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact * i
#     print(fact) 

# factorial(5)   

# # =======================================================
# Question 3:

# def square(number):
#     return [num ** 2 for num in number]

# print(square([1,2,3,4,5]))

# =======================================================
# Question 4:


# =======================================================
# Question 5:

# def cube(*number):
#     for n in number:
#         print(n ** 3)

# cube(2,3)

# =======================================================
# Question 6:

# def add(*args):
#     return "Sum:",sum(args)

# print(add(13,14,46,67))

# =======================================================
# Question 7:

# def name_list(*args):
#     if len(args) == 0:
#         print("List is empty.")
#     else:
#         for name in args:
#             print(name)

# name_list("Alice","Barbie","charlie")

# =======================================================
# Question 8:

# def strings(*args):
#     strings_1 = tuple(filter(lambda x: type(x) == str, args))
#     number = tuple(i for i in args if type(i) == int or type(i) == float)
#     return(strings_1,number)


# print(strings("alice",12,35,"barbie"))

# =======================================================
# Question 9:

# def info(*kwargs):
#     details = {
#         "name" : input("Enter your name: "),
#         "age" : int(input("Enter your age: ")),
#         "city" : input("Enter your city: ")
#     }

#     return details

# print(info())

# =======================================================
# Question 10:

# def cost(**kwargs):

#     total = kwargs["price"] * kwargs["quantity"]
#     print(f"\nProduct Name: {kwargs["name"]}")
#     print(f"Product Price: {kwargs["price"]}")
#     print(f"Product Quantity: {kwargs["quantity"]}")
#     print(f"Total cost: {total}")
        
# cost(name = "Laptop" , price = 500000 , quantity = 2)
# cost(name = "Moblie" , price = 150000 , quantity = 3)

# =======================================================
# Question 11:

# def info(**kwargs):
#     if "name" in kwargs and "department" in kwargs and "salary" in kwargs:
#         print("Name:",kwargs["name"])
#         print("Deapartment:",kwargs["department"])
#         print("Salry:",kwargs["salary"])
#     else:
#         print("please enter all details.")

# info(name = "Alice", department = "Sales", salary = 200000)

# =======================================================
# Question 12:

# def area(lenth,width):
#     """
#     calulate the aera of a rectangle.
#     """
#     return(lenth * width)

# print(area.__doc__)
# print(area(10,5))

# =======================================================
# Question 13:

# def fibonnaci(num):

# """
# Calculate and display the Fibonacci series.
# """
#     a = 0
#     b = 1

#     for i in range(0,num):
#         print(a,end=" ")
#         c = a + b
#         a = b
#         b = c
        
# fibonnaci(5)