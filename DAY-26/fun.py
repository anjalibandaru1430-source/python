#decorator is function - it takes one function as input and modified function as a output
def login_reg(func):
    def inner(name,st):
        if st!=True:
            print('Login reg')
        else:
            return func(name,st)
    return inner

def index(name,str):
    print("Home page is created")

def product_page(name,str):
    print("Product page ")
    
@login_reg
def order_page(name,str):
    print("Placed order")
@login_reg  
def profile(name,str):
    print("Profile page")

index("rahul",False)
product_page("rahul",True)
order_page("RG",False)
profile("RG",False)