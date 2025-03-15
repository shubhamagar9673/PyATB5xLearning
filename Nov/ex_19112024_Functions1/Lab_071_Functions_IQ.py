def sum_of_three(a=1, b=1, c=1):
    return a + b + c


result1 = sum_of_three()
print(result1)

result2 = sum_of_three(1, 2)
print(result2)

result3 = sum_of_three(1, 2, 3)
print(result3)

result4 = sum_of_three(1, 2, 3, 4)  # this will give error
print(result4)
