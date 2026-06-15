#highest even number
li = [2,10,4,623,9,21,92,83]
def highest_even(li):
    even_num = []

    for num in li :
        if num % 2 == 0 :
            even_num.append(num)
    return max(even_num)
print(highest_even(li))
