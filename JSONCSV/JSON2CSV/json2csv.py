import csv
import json

fp1=open('emp.json','r')
employees=json.load(fp1)
print(type(employees))
print(type(employees))

female_employees=[]
for  emp in employees:
    female_employees.append([emp['id'],
                             emp['ename'],
                             emp['gender']])
    print(female_employees)

