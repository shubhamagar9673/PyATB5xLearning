for i in range(0,10,1):
    if i==6 or i==5:
        print(i)
    else:
        pass  #Skip And do nothing

    """
                   |i| condition | o/p
                   |0| 0==6->False or 0==5->False| o/p = blank/nothing
                   |1| 1==6->False or 1==5->False| o/p = blank/nothing
                   |2| 2==6->False or 2==5->False| o/p = blank/nothing
                   |3| 3==6->False or 3==5->False| o/p = blank/nothing
                   |4| 4==6->False or 4==5->False| o/p = blank/nothing
                   |5| 5==6->False or 5==5->True| o/p = 5
                   |6| 6==6->True  or 6==5->False| o/p = 6
                   |7| 7==6->False or 7==5->False| o/p = blank/nothing
                   |8| 8==6->False or 8==5->False| o/p = blank/nothing
                   |9| 9==6->False or 9==5->False| o/p = blank/nothing
                   

                   """