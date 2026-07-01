def remove_duplicate(lst):
    unique = []
    for item in lst :
        if item not in unique:
            unique.append(item)
    return unique
print(remove_duplicate([1,2,3,3,5,4,5,4,6,6]))