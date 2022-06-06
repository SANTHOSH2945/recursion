def decimaltobinary(n):
    assert int(n)==n,'the parameter must be an integer!'
    if n == 0:
        return 0
    else :
        return int(n%2)+(10*decimaltobinary(int(n/2)))
print(decimaltobinary(1000))
