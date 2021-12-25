def factorial(num):
    fact = 1
    if num == 0:
        print("Factorial of %s is 1: " %num)
    else:
        for value in range(1,num+1):
            fact = fact*value
        
        print("Factorial of %s is:" %num,fact)

factorial(11)