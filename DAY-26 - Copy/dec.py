def smart_dev(func):
    def inner(a,b):
        if b==0:
            print("cant divide by 2")
        else:
            return func(a,b)
    return inner

#@smart_dev
def division(a,b):
    print(a/b)
    print("hellomyworld")

division(10,2)

def division(a,b):
    print(a/b)
    print("hellomyworld")

division(10,5)
