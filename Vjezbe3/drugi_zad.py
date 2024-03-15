def iteracije(n):
    p1=5
    p2=5
    for i in range(0,n):
        p1=p1+1/float(3)
    for i in range(0,n):
        p2=p2-1/float(3)
    return [p1,p2]

print(iteracije(20))
print(iteracije(2000))
print(iteracije(20000))