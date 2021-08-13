day=input("enter the day")
if day=="thusday":
    print("going outside")
    place=input("enter the place")
    if place=="katrejh":
        print("ja skte hai")
        senior=input("enter the purmision")
        if senior=="yes":
            print("purmision done")
            sefty=input("enter the preqution")
            if sefty=="mask":
                print("yes this is sefty")
                time=int(input("enter the time"))
                if time==6:
                    print("come before 6")
                    reason=input("enter the problem")
                    if reason=="health issue":
                        print("purmission mil skti hai")
                    else:
                        print("nhi mil skti")  
                else:
                    print("not come") 
            else:
                print("this is not sefty") 
        else:
            print("purmision is not done") 
    else:
        print("nhi ja skte")  
else:
    print("not going outside")               


        
