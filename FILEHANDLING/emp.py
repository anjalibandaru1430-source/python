import json
emp={
    'eid':101,
    'ename':"RAHUL",
    'esal':45000.45,
    'avail':True,
    'discount':None
}
#json to python =load() or loads()
#dump - file handling
#dupms - convertions ,type casting
emp_json_str=json.dumps(emp)
print(emp_json_str)