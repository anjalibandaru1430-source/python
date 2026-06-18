import csv
employees=[
    [1,"Anu","Female"],
    [2,"rahul","Male"]
]

fp=open('user.csv','w',newline="")
csv_writer=csv.writer(fp)
csv_writer.writerow(["uid","uname","gender"])
csv_writer.writerows(employees)
print("new csv file created")
