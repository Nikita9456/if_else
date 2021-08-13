print("welcome to SBI")
card=input("insert the card")
print("insert the card")
if atmcard=="debit":
    print("incurrect pin")
else:
    ("please deside your langueuage")
print("card inserted")
language=input("enter the languege")
if language=="hindi" or language=="english":
    print("it is your language")
    pin=int(input("enter the pin"))
    if pin==1234:
        print("your pin is correct")
        accountttype=input("enter the typr of account")
        if accounttype=="saving":
            print("your accunt is saving")
        elif accounttype=="current":
            print("your account is current")
        withdrawl=int(input("enter the ammount"))
        if withdrawl<=150000:
            print("amount is available")
            balence=input("want to cheak balence")
            if balence=="yes":
                print("your blance is 300000")
                recipt=input("want recipt ")
                if recipt=="yes":
                    print("take your recipt")
                else:
                    print("ok")
            else:
                print("insult failed balance")
        else:
            print("incurrect pin")
    else:
        ("please deside your langueuage")

