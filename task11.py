students = [
    {"id" : 101, "name" : "Alice", "score" : 85},
    {"id" : 102, "name" : "Bob", "score" : 78},
    {"id" : 103, "name" : "Charlie", "score" : 92}
]

for data in students:
    print(data)
print()

avg = sum(data["score"] for data in students) /len(students)
print("Average Score:",avg)
print()

students.append({"id" : 104, "name" : "Dhairya", "score" : 90})
for data in students:
    print(data)
print()

students[1]["score"]= 102
for data in students:
    print(data)
print()

students.pop(2)
for data in students:
    print(data)
print()

for data in students:
    if data["score"] > 80:
        print(data)
print()

# students.sort(reversed=True)    it is false
# print(students)

highest = students[0]

for data in students:
    if data["score"] > highest["score"]:
        highest = data
print(highest)
print()


for data in students:
    if data["score"] >= 90:
        grade = "A"
    elif data["score"] >= 80:
        grade = "B"
    else:
        grade = "C"
    print(f"Name: {data["name"]} | Score: {data["score"]} | Grade: {grade}")
print()

grade_count = {"A":0, "B":0, "C":0}
for data in students:
    if data["score"] >= 90:
        grade = "A"
    elif data["score"] >= 80:
        grade = "B"
    else:
        grade = "C"

    grade_count[grade] += 1

print(f"A Grade: {grade_count['A']}")
print(f"B Grade: {grade_count['B']}")
print(f"C Grade: {grade_count['C']}")

