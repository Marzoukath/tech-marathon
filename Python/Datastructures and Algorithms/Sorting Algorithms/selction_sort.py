arr = [25, 65, 13, 90, 55, 10]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if(arr[i] > arr[j]):
           min_index = j
           arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)