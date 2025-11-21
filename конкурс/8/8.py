def sol_sakura(line=['10.04', '15.04', '20.04']):
    def updown(x,y):
        x,y = [int(i) for i in x.split('.')],[int(i) for i in y.split('.')]
        if x[1]==y[1]:
            if x[0]<y[0]:
                return 1
            else:
                return -1
        elif x[1]<y[1]:
            return 1
        elif x[1]>y[1]:
            return -1
    l,a,b = [],[],[]
    for j in range(len(line)):
        if updown(line[j-1],line[j]) == 1:
            if len(a)>1:
                l.append(a)
            a = []
        if updown(line[j-1],line[j]) == -1:
            if len(b) > 1:
                l.append(b)
            b = []
        a.append(line[j])
        b.append(line[j])
        if j == len(line)-1 and len(a)>1:
            l.append(a)
        elif j == len(line)-1 and len(b)>1:
            l.append(b)
        print(a,b)
    print(l)
sol_sakura()

# if updown(line[j - 1], line[j]) == c:
#     print(line[j - 1], line[j], a, '-')
#     if len(a) > 1:
#         l.append(a)
#     c = -c
#     a = [line[j - 1]]