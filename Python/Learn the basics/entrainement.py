age = int(input("How old are you? "))
if age < 18:
    print("you're minor.")
else:
    print("you're adult")

#2
sm = 0
for i in range(1, 10001):
    sm += i
    
print(sm)

#3
sm=0
for i in range(1,1001):
    if(i%7 == 0):
        sm += i
print(sm)

#4

sm=0
n=2
while(sm <= 2023 ):
    n += 1
    for i in range(1,n+1):
          sm += i    
print(n)
print(sm)

