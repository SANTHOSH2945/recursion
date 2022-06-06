
def productOfArray(arr):
    k = 1
    for i in arr:
        k = k*int(i)
    return k

print(productOfArray([1,2,3,10]))
