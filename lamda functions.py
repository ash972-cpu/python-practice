li = [1,2,3,4,5,6,7,8,9]
def is_odd(items):
    return items % 2 != 0
print(tuple(filter(is_odd,li)))
print(li)
