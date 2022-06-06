def power(base,exp):
    assert exp>=0 and int(exp)==exp,'The number should be positive integer!'
    if exp == 0 :
        return 1
    if exp == 1:
        return base
    else:
        return base*power(base,exp-1)
m = input('enter base value')
n = input('enter exponent value')

print(power(int(m),int(n)))
