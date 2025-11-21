def sol_factorial(M):
    M = str(M)
    fac = {
        1: "1",
        2: "2",
        3: "6",
        4: "24",
        5: "120",
        6: "720",
        7: "5040",
        8: "40320",
        9: "362880",
        10: '3628800'
    }
    for i in fac:
        if all(x in fac[i] for x in M):
            g = -1
            o = 0
            for x in M:
                if fac[i].find(x) > g:
                    o += 1
                    g = fac[i].find(x)
                elif fac[i].find(x, fac[i].find(x)+1) > g:
                    o += 1
                    g = fac[i].find(x, fac[i].find(x)+1)
            if o == len(M):
                return (i, len(fac[i])-len(M))
    return (-1, -1)
print(sol_factorial(388))