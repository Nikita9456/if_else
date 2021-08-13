a=int(input("enter the price"))
b=int(input("enter the price"))
c=int(input("enter the price"))
if a>=b:
    if a>=c:
        print("a is highest price")
elif b>=a:
    if b>=c:
     print("b is highest price")
    else:
        print("c is highest price")