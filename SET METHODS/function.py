def outer():
    print("outer function started")
    def login():
        print("inner function started")
    return login
inner = outer()
print(inner)
inner()
inner()