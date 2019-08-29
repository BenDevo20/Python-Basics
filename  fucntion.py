def add_10(m):
    if m >= 100:
        m = m + 10
        return m
    else:
        return "save more!"
print(add_10(10))

def subtract(a,b,c):
    result = a - b * c
    print("A = ", a)
    print("B = ", b)
    print("C = ", c)
    return result
print(subtract(1,2,3))
