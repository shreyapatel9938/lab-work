# Question 1:
for i in range(1,21):
    if(i % 4 == 0):
        continue
    print(i)
print()


# ===================================================
# Question 2:
num = 1
while (num <= 10):
    if (num == 7):
        break
    print(num)
    num += 1
print()

# ===================================================
# Question 3:
data = "PYTHON"
for i in data:
    if i in "AEIOU":
        continue
    print(i)
print()

# ===================================================
# Question 4:
num = int(input("Enter the value of number: "))

for i in range(1,num+1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()
print()
# ===================================================
# Question 5:
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

# ===================================================
# Question 6:
for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j,end=" ")
    print()
print()

# ===================================================
# Question 7:
for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end=" ")
    print()
print()
  
# ===================================================
# Question 8:
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()
print()
