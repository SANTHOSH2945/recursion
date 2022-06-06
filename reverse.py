def reverse(strng):
    if len(strng) == 0:
        return strng
    else:
        return reverse(strng[1:]) + strng[0]
print(reverse('santhosh'))
