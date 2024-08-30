fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x :
        new_list.append(x)
print(new_list)


# With list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

numbers= [3, 4, 5, 8, 9 ,10, 15]
new_list = [x for x in numbers if x<8]
print(new_list)
 
newlist = [x for x in range(10)]
#Set all values in the new list to 'hello'
newlist = ['hello' for x in fruits]

print(newlist)
s = 'Hello World!'
l = [_s.upper() for _s in s[:-1]]

print(l)
l = [[i for j in range(2)] for i in range(3)]

print(l)