def prime_number(num):
    count = 0 
    for i in range(3,num):
        if  num % i == 0:
            count = count + 1
            break

    
    if count == 0:
        print(num, "is prime number")
    else:
        print(num, "is not a prime number")
        



prime_number(10)