import csv

fp=open('emp.csv','r')

emp_data=csv.reader(fp)
type(emp_data)
employees=list(emp_data)
for emp in employees[1:]:
    print(emp[1])


#employees=csv.DictReader(fp)

'''for employee in employees:
    if employee ['gender']=='Male':
        print(employee)'''

'''for employee in employees:
    if employee ['gender']=='Female':
        print(employee)'''






