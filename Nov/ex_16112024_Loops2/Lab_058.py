from collections import Counter

for i in range(101): # value will go from 0 to 100
    if i%2 ==0:
        print(i)


        """
        |i| condition | o/p
        |0| 0%2==0 ->True| o/p->0
        |1| 1%2==0 ->False| o/p->Nothing will be printed
        |2| 2%2==0 ->True| o/p->2
        |3| 3%2==0 ->False| o/p->Nothing will be printed
       
        """