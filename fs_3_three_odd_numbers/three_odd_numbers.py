def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    new_nums = 0
    #odd_num = []

    #for n in range(1,50,2):
        #odd_num.append(n)


    
    for n in nums:
        if n == 0 or n % 2 != 0:
            new_nums += n
    
    print(new_nums)
    if new_nums % 2 != 0:
        return True
    else:
        return False

            


