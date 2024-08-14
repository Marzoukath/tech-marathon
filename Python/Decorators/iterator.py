# define a list
my_list = [4, 7, 0]
# create an iterator from the list
iterator = iter(my_list)
# get the first element of the iterator
print(next(iterator))  # prints 4
# get the second element of the iterator
print(next(iterator))  # prints 7
# get the third element of the iterator
print(next(iterator))  # prints 0


my_list = [4, 7, 0]
print("Print iterator by using a loop")
for element in my_list:
    print(element) # print each element


print('building custom iterators')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)




print('Use python infinite iterator')

from itertools import count
# create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)
# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))
