#Lambda

# when use normal function

def triple_me(num):
    return num**3
result = triple_me(2)
print(result)


#now same thing we can do using lambda function as below

result_l = lambda num:num**3
print(result_l(2))

