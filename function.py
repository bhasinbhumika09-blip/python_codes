def goodDay(name):
    print("Goodday "+name)
goodDay("Bhumika")   #function call
goodDay("Swastika")
goodDay("Riya")

def greet(name):
    gr="Hello "+name
    return gr
a=greet("Bhumika")
print(a)

def greet(name,ending="Thankyou"):
    print(f"Goodday, {name}")
    print(ending)
greet("Bhumika")
