def sol_3dprint(a,b):
    s = []
    for z in range(-10000,10000+1):
        z = round(z*0.0001, 5)
        f = ((1-(z**2))**0.5)/(a*(b**z))
        s.append((f**3)*(4/3)*3.14)
    return sum(s)
print(sol_3dprint(1.6,1.4))
