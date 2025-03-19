#Count vowels from i/p string

# a,e,i,o,u

input_string = "Hello, World !"


vowels = "aeiou"

vowels_count = 0
result= dict()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count +1

print(vowels_count)
