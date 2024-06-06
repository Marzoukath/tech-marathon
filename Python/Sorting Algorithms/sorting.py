numbers = [23, 56, 2, 90, 65, 76, 20, 4]
sort = []

while numbers :
    m = min(numbers)
    sort.append(m)
    i = numbers.index(m)
    del numbers[i]
print(sort)

print(sorted ([20, 5, 7, 90]))