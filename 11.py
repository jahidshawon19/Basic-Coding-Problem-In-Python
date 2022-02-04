salary = [5000,7000,10500,15000,20000,25000,30000,35000]
sum = 0
total_elements = len(salary)
for i in salary:
    sum = sum + i

print('Sum: {}, Average: {}'.format(sum, sum/total_elements))