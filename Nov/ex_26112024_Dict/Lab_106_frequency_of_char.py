#Frequency of char in a string

string = "automation"

#{a:2,u:1,t:2,o:2,m:1,i:1,n:1}  this is the answer

char_count = {}

#Logic Building
#I/P-->String
# O/P-->Dictionary

for char in  string:
    char_count[char] = char_count.get(char, 0) +1
    print(char_count)




