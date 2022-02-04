def count_digit(num):
    temp = num 
    count = 0 
    while temp != 0:
        temp = round(temp / 10)
        count += 1
    
    print(count)


message = "Enter Your Digit:  "
num = input(message)
num = int(num)

count_digit(num)