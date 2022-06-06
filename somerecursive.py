def isOdd(num):
    for i in num:
        if (int(i))%2==0:
            return False
        else:
            return True

def someRecursive(arr, cb):
    cd = isOdd(arr)
print(someRecursive([1,2,3,4],isOdd))
