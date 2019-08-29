even = [0,2,4,6,8,10,12,14,16,18,20]
for n in even:
    print(n)

x = 0
while x <= 20:
    print(x) # this will print an infinite amount of 0s
    x = x+2 # this continues to print until it reaches 20
    x  += 2 # this does the same thing as the oeprator above

for n in range(10):
    print(2**n)

for x in range(20):
    if x % 2 == 0:
        print(x)
    else:
        print("odd")

x = [0,1,2]
for item in x:
    print(item)