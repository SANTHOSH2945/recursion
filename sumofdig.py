def sumofdigit(n):
    assert n>=0 and int(n)==n,'only for positive integer'
    if n in range(0,10):
        return n
    else:
        return int(n%10) + sumofdigit(int(n/10))
k = input('enter any digit number')
print(sumofdigit(int(k)))
