s = ['VLADIVOSTOK', 'AVATAR']
t = ['TOKYO', 'VLADISLAV', 'VLAD', 'STOKS']
# def front_match(x,y):
#     n = 0
#     # if len(x) >= len(y):
#     #     g = [x[i] for i in range(len(y)) if x[i]==y[i]]
#     # elif len(x) < len(y):
#     #     g = [x[i] for i in range(len(x)) if x[i] == y[i]]
#     g = []
#     for i in x:
#         for j in y[::-1]:
#             if i == j:
#                 n += 1
#                 g.append(i)
#             else:
#                 return n, g
# def back_match(x,y):
#     n = 0
#     for i in x[::-1]:
#         for j in y:
#             if i == j:
#                 n += 1
#             else:
#                 return n

# def front_match(x,y):
#     if x[0:len(y)]==y:
#         return x[0:len(y)]
#     else:
#         for i in range(len(y)):
#             if x[0:i]!=y[::-1][0:i]:
#                 return x[0:i], y[::-1][0:i]

def front_match(x,y):
    for i in range(len(y)):
        if y[i]==x[0]:
            if y[i:]==x[0:len(y[i:])]:
                return y[i:],x[0:len(y[i:])], i
def end_match(x,y):
    x = x[::-1]
    for i in range(len(y)):
        if y[i]==x[0]:
            if y[i:]==x[0:len(y[i:])]:
                return y[i:],x[0:len(y[i:])], i
print(end_match('ABABACA','ABACA'))
# res = [[j for j in t if front_match(i,j) or back_match(i,j)] for i in s]
# print(res)