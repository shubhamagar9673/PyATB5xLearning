# find the first non-repeating char using sets from a string
# swiss--> hare s is not the answer as it is repeating so the answer is W

def first_non_repeating_letter(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None
print(first_non_repeating_letter("swiss"))
print(first_non_repeating_letter("pepper"))
print(first_non_repeating_letter("dada"))
