# recursive method
def uToptRec(n,h=0):
    if n < 0:
        return h
    return uToptRec(n-1, h+1 if n%2==0 else h*2)

print(uToptRec(5))  


#iterative method
def uTopianTree(n):
    h=0
    for a in range(n+1):
        if a%2 == 0:
            h+=1
        if not a%2 == 0:
            h*=2
    return h
