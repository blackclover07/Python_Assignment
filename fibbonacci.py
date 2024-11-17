def fiboonacci(num):
    fib_series=[0,1]
    
    for i in range(2,num):
        next_fib_num=fib_series[i-1]+fib_series[i-2]
        fib_series.append(next_fib_num)
    return fib_series


fib_range=int(input("Enter the range : "))
fibbo_series=fiboonacci(fib_range)

print(fibbo_series)