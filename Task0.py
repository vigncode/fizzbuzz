for i in range(1,101):
    '''
    fizz = ""
    buzz=""
    if i%3 == 0:
        fizz="Fizz"
    if i%5 == 0 :
        buzz= "Buzz"
    
    if fizz is not "" or buzz is not "":
        print(fizz+buzz)
    else:
        print(i)
    
    '''
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