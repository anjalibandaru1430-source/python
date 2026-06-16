from random import choice,choices

enames=["Anu","Rahul","Anjali","Ammu","Nani","vijay"]
luck_names=choice(enames)
print(luck_names)

luck_draw_list=choices(enames,k=3)
print(luck_draw_list)