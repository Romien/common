""" 
Tested 11 functions with unittests in unit_tests.py and 9 functions with pytest 
in test_pytests.py.
"""


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


def convert_num(num):
    """
    Task 11:
    Write a program that will take the num parameter being passed and return the number of
    hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    hour, minute = divmod(num, 60)
    return "{}:{}".format(hour, minute)


def largest_word(s):
    """
    Task 12:
    Write a program that will take the parameter being passed and return the largest word 
    in the string. If there are two or more words that are the same length, return the first 
    word from the string with that length. Ignore punctuation.

    Sample Test Cases:

    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love 
    """
    import string

    x = s.translate(str.maketrans('', '', string.punctuation))
    new_arr = x.split(' ')
    return max(new_arr, key=len)


def backwards(s):
    """
    Task 13:
    Write a program (using functions!) that asks the user for a long string containing 
    multiple words. Print back to the user the same string, except with the words in 
    backwards order.

    For example:
    Input: My name is Michele
    Output: Michele is name My
    """
    return " ".join(s.split()[::-1])


def fibonacci_seq_task_14():
    """
    Task 14:       
    Write a program that asks the user how many Fibonnaci numbers to generate and then 
    generates them. Take this opportunity to think about how you can use functions. Make 
    sure to ask the user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
    sequence is the sum of the previous two numbers in the sequence. The sequence looks 
    like this: 1, 1, 2, 3, 5, 8, 13, …)
    """
    num = int(input("Enter the number: "))
    n1, n2 = 0, 1
    for i in range(num):
        n1, n2 = n2, n1 + n2
        return n1
    # n = input("How many Fibonacci numbers to generate? ")
    # a, b = 0, 1
    # for i in range(int(n)):
    #     a, b = b, a + b
    #     print(a, end=', ')


def even_numbers(a):
    """
    Task 15:       
    Let’s say I give you a list saved in a variable: 
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this 
    list a and makes a new list that has only the even elements of this list in it.
    """
    return [i for i in a if i % 2 == 0]


def add_to_input(num):
    """
    Task 16:
    Write a program that will add up all the numbers from 1 to input number. For example: 
    if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10 
    """
    count = 0
    for i in range(1, num + 1):
        count += i
    return count


def factorial(num):
    """
    Task 17:       
    Write a program that will take the parameter being passed and return the factorial 
    of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def change_letter(letters):
    """
    Task 18:       
    Write a program that will take the str parameter being passed and modify it using the
    following algorithm. Replace every letter in the string with the letter following it 
    in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this 
    new string (a, e, i, o, u) and finally return this modified string.
    Input: abcd
    Output: bcdE 
    """
    new_str = ""
    for l in letters:
        new_l = chr(97 if l == 'z' else ord(l) + 1)
        if new_l in ('a', 'e', 'i', 'o', 'u'):
            new_l = new_l.capitalize()
        new_str += new_l
    return new_str


def alphabet_order(s):
    """
    Task 19:       
    Write a program that will take the str string parameter being passed and return the 
    string with the letters in alphabetical order (ie. hello becomes ehllo). Assume 
    numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    """
    return ''.join(sorted(s))


def compare_numbers(num1, num2):
    """
    Task 20:       
    Write a program that will take both parameters being passed and return the true if 
    num2 is greater than num1, otherwise return the false. If the parameter values are 
    equal to each other then return the string -1
    """
    if num1 < num2:
        return True
    elif num1 == num2:
        return '-1'
    else:
        return False
