for number in range(10):  # 0 to 9
    if number % 2 == 0:
        continue
    else:
        print(number)

    """
     | i | condition | o / p
     | 0 | 0%2 ==0 ->True| continue-Skip no o/p
     | 1 | 1%2 ==0 ->False| 1
     | 2 | 2%2 ==0 ->True| continue-Skip no o/p
     | 3 | 3%2 ==0 ->False| 3
     | 4 | 4%2 ==0 ->True| continue-Skip no o/p
     | 5 | 5%2 ==0 ->False| 5
     | 6 | 6%2 ==0 ->True| continue-Skip no o/p
     | 7 | 7%2 ==0 ->False| 7
     | 8 | 8%2 ==0 ->True| continue-Skip no o/p
     | 9 | 9%2 ==0 ->False| 9
     """
