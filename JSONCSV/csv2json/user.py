import csv
import json
fp1=open('user.csv','r')
csv_reader_obj=csv.reader(fp1)
#extract
users=list(csv_reader_obj)
#transform
employee_data=[]
#how to exclude csv header ? user 
for user in users[1:]:
    employee_data.append({
        "eid":user[0],
        "ename":user[1],
        "gender":user[2]
    })
#load into new json file
print(employee_data)
fp2=open('emp.json','w')
json.dump(employee_data,fp2)
print(" new Enjoy weekend")
