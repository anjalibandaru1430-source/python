#read emp.json file and print all employess names
#dump is for python object 


import json

fp=open('emp.json','r')
employees=json.load(fp)

'''for emp in employees:
    print(emp['ename'])'''

for emp in employees:
    if emp ['gender']=='Male':
        print(emp['ename'],"_",emp['gender'])