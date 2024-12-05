# 1 concatenate two lists
list1 = [1, 3, 5, 7, -3]
list2 = [9, 11, 13 ,14]

list3 = list1 + list2
print(list3)


#2
l = [1, 5, 6,  9, 0, 5, 70]
max = 1

for i in l:
    if i > max :
        max = i

print (max)


person = { 'name': 'John Doe',
           'age':  '30'

}
print(f"Name: {person['name']}")