def sum(n):
    assert n>=0 and int(n)==n,'please proceed with positive integer'
    if n in [0,1]:
        return n
    else:
        return n+sum(n-1)
k = input('enter the value of the number')
print(sum(int(k)))
