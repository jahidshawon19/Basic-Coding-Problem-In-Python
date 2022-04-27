def common_letters(s1, s2):
    # remove duplicate 
    string1 = set(s1)
    string2 = set(s2) 

    # Find Common letter using & 
    result = string1 & string2 
    print(result) 



str1 = input("Enter First String")
str2 = input("Enter Second String") 

common_letters(str1, str2) 