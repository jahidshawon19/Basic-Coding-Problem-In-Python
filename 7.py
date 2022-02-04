
def sum_digit(num):
    sum = 0
    temp = num 

    while temp != 0:
        rem = temp % 10 
        sum = sum + rem 
        temp = temp / 10 
    
    return sum 



message = "Enter a digit: "
num = input(message)
num = int(num)

result = sum_digit(num)
print('Sum of', num, 'is:', int(result))

