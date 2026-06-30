import json
f1=open('students.json','r')

students=json.load(f1)

# for student in students:
#     print(student)

# for student in students:
#     print(student['name'])

# for student in students:
#     if student['cgpa']>8.0:
#         print(student['name'])


# male and female students
#male
# for student in students:
#     if student['gender'] == "Male":
#         print(student['name'])

#female
# for student in students:
#     if student['gender'] == "Female":
#         print(student['name'])


#count
# count_male=0
# count_female=0
# for student in students:
#     if student['gender']=="Male":
#         count_male+=1
#     else:
#         count_female+=1


# print(f"male students:{count_male}")
# print(f"female students:{count_female}")


#find student by id

# n=int(input("enter a id "))
# for student in students:
#     if student["id"]==n:
#         print(student['name'],student['cgpa'])
        
#find student by city
city=input("enter cityt")
for student in students:
    if student["city"]==city:
        print(student['name'])
