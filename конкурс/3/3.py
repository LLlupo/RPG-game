a = 12
b = 16
c = 1333
def sol_detox(a,b,c):
    s = []
    for x in range(0,c):
        for y in range(0, c):
            if x*a + y*b == c:
                s.append((x,y))
    return s
print(sol_detox(a,b,c))