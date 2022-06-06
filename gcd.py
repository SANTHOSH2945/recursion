def gcd(a,b):
    assert int(a)==a and int(b)==b,'enter the integers only'
    if a<0 :
        a = -1*a
    if b<0 :
        b = -1*b
    if b == 0:
        return a
    #if a == b:
    #    return a
    else:
        return gcd(b , int(a % b))
print(gcd(-64,24))
