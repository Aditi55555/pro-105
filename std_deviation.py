import math
import csv

with open ('data.csv',newline ='') as s:
    reader = csv.reader(s)
    file_data = list(reader)
    
data = file_data[0]

#finding mean

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    
    mean = total/n
    return mean

#squaring and getting the value (xi-mean)^2

squaredlist = []
for a in data:
    num = int(a)-mean(data)
    num = num**2
    squaredlist.append(num)

#Getting the sum
sum = 0
for y in squaredlist:
    sum += y

#dividing the sum by n-1
result = sum/(len(data)-1)

#getting the square root of the result
standarddeviation = math.sqrt(result)
print(standarddeviation)