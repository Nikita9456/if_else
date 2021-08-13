year=int(input("enter the year"))
if year%4==0:
    print("it is the leap year")
elif year%100==0:
    if year%400==0:
        print("it is the leap year") 
    else:
         print("not a leap yeap")
else:
    print("not a leap year")               2020
    