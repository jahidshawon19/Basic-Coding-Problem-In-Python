lucky_numbers = [12,47,85,69,78,25,36,49,10,23]
square = []
cube = []

for i in lucky_numbers[:5]:
    i=i**2
    square.append(i)

for j in lucky_numbers[5:]:
    j=j**3
    cube.append(j)

combined_lists = zip(square, cube)
total = [a+b for(a,b) in combined_lists]
print(total)