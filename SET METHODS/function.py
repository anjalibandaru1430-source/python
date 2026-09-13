def outer():
    print("outer function Started")
    def login():
        print("inner function Started")
    return login
inner = outer()
print(inner)
inner()
inner()