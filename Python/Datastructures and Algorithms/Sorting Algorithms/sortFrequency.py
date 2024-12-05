class ele:
    def __init__(self):

        self.count = 0
        self.index = 0
        self.val = 0


def mycomp(a):
    return a.val

element = [2,3,5,6,4,6,2,6]

elr= [None for _ in range(len(element))]
for i in range(len(element)):
    elr[i] = ele()
    elr[i].val = element[i]
elr.sort(key=mycomp)
sorted_values = [e.val for e in elr]
print(sorted_values)