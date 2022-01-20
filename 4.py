from audioop import reverse


num = [10,40,50,20,20,30,40,10,50,60,70,70,60]

def remove_duplicate(data):
    unique_num = []
    for i in data:
        if i not in unique_num:
            unique_num.append(i)
    
    return unique_num


# print(remove_duplicate(num))



