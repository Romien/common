def common_in_lists(list1, list2):
    """
    Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
      and write a program that returns a list that contains only the elements that are common 
      between the lists (without duplicates).
      """

    return list(set(list1).intersection(list2))


def check_a(s):
    """
    Return the number of times that the letter “a” appears anywhere in the given string.
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    return s.count('a')


def check_power(n):
    """
    Write a Python program to check if a given positive integer is a power of three.
        Input : 9
        Output : True
    """
    while (n % 3 == 0):
        n /= 3
    return n == 1


def add_digits(n):
    """
    Write a Python program to add the digits of a positive integer repeatedly until the result
    has a single digit.
    Input : 48
    Output : 3
    """

    while len(str(n)) != 1:
        n = sum([int(i) for i in str(n)])
    return n


def move_zeroes(list_1):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    for i in list_1:
        if i == 0:
            list_1.remove(0)
            list_1.append(0)
    return list_1


def check_progression(l):
    """
    Task 6:
    Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    """
    if len(l) < 2:
        return False
    else:
        diff = l[1] - l[0]
        for i in range(len(l) - 1):
            if not (l[i + 1] - l[i]) == diff:
                return False
        return True


def single_num(l):
    """
    Task 7:
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    for i in l:
        if l.count(i) == 1:
            return i


def missing_num(l):
    """
    Task 8:
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    return sum(range(l[0], l[-1] + 1)) - sum(l)


def count_elem(l):
    """
    Task 9:
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    count = 0
    for num in l:
        if isinstance(num, tuple):
            break
        count += 1
    return count


def reverse_order(s):
    """
    Task 10:
    Write a program that will take the str parameter being passed and return the string in 
    reversed order. For example: if the input string is "Hello World and Coders" then your 
    program should return the string sredoC dna dlroW olleH.
    """
    return s[::-1]
