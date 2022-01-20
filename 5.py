data = [125,135,145,155,165,175,185,195]


def reverse_list(li):
    list_len = len(li)
    for i in range(int(list_len/2)):
        temp = li[i]
        li[i] = li[list_len-i-1]
        li[list_len-i-1] = temp 
    
    return li 


print(reverse_list(data))



