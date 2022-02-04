my_list = [0,1]
num=int(input("Enter a number: "))

for i in range(2, num):
    my_list.append(my_list[i-1]+my_list[i-2])

print(my_list)