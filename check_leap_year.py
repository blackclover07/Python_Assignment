def is_leap_year(year):
        if(year%4==0 and year%100 !=0) or (year%400==0):
                return True
        else:
                return False
            
            

year = int(input("Enter the Year : "))

result=is_leap_year(year)

if(result):
    print("Leap Year")
else:
    print("Not Leap Year")