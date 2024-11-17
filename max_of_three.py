def max_of_three():
    numbers=[]
    for i in range(3):
        while True:
            try:
                number=int(input(f"Enter number {i+1} : "))
                numbers.append(number)
                break
            except ValueError:
                print("Please Enter numbers only")
    max_num=max(numbers)
    print(f"Max number is : {max_num}")
    
    
max_of_three()