numbers = [10,18,20,22,24,27,31,32,36]
n = len(numbers)
position = -1
search_number = int(input("Enter a number: "))

for i in range(0, n):
    if search_number == numbers[i]:
        position = i+1 
        break

if position == -1:
    print("Sorry Not Found")
else:
    print("{} Found at position {}".format(search_number, position))