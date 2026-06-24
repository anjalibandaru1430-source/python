import requests,json
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
#print(len(users))
#print(users)

#Transform
users_json=[]
for user in users:
    users_json.append({
        "uid":user['id'],
        "name":user['username'],
        "city":user['address']['city'],
        "company":user['company']['name']
    })
print(len(users_json))
print(users_json)


fp1=open('user.json','w')
json.dump(users_json,fp1)
print("New Data file created")