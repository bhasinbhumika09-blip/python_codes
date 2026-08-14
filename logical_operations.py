a1=int(input("Enter no.1:"))
a2=int(input("Enter no.2:"))
a3=int(input("Enter no.3:"))

if(a1>a2 and a1>a3):
    print("a1 is greater than a2 and a3")

elif(a1>a2 and a1<a3):
    print("a1 is greater than a2 and smaller than a3")

elif(a1<a2 and a1>a3):
    print("a1 is greater than a3 and smaller than a2")

elif(a2>a1 and a2>a3):
    print("a2 is greater than a1 and a3")

elif(a2>a1 and a2<a3):
    print("a2 is greater than a1 and smaller than a3")

elif(a2<a1 and a2>a3):
    print("a2 is greater than a3 and smaller than a1")

elif(a3>a1 and a3>a2):
    print("a3 is greater than a1 and a2")

elif(a3>a1 and a3<a2):
    print("a3 is greater than a1 and smaller than a2")

else:
    print("a3 is greater than a2 and smaller than a1")
