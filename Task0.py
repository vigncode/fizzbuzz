for i in range(1,101):

    a=i%3
    b=i%5
    status =i
    if a==0 and b ==0:
        status = "FizzBuzz"
    elif a==0:
        status = "Fizz"
    elif b==0:
        status = "Buzz"
    
    print(status)