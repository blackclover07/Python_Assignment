def division_calculation():
    print("Enter the marks of 4 subjects(marks should be between 0 to 100)")
    
    marks=[]
    
    for i in range(4):
        while True:
            try: 
                mark=float(input(f"Enter Subject {i+1} marks : "))
                if( 0 <= mark <=100):
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 to 100")
            except ValueError:
                print("Invalid input please enter a number between 0 to 100")
                
    total_marks=sum(marks)
    
    percentage=(total_marks/400)*100
    
    if percentage>=75:
        division="Division 1"
    elif 65<=percentage<75:
        division="Division 2"
    elif 50<=percentage<65:
        division="Division 3"
    else:
        division="Failed"
    
    
    print(f"Total marks : {total_marks}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Division : {division}")
    


division_calculation()