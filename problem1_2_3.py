"""
isPalindrome takes in a positive integer and returns True or False if the 
number is a palindrome. puzzle1 computes and prints the three numbers.
make_palindromes returns a list of palindromes, and puzzle2 solves the puzzle.

Puzzle1 Iterations: 979
Puzzle2 Iterations: 87
"""

def isPalindrome(x):
    x = str(x)
    y = x[::-1]
    if y == x:
        return True
    else:
        return False


def puzzle1():
    twodigitpal = 0
    threedigitpal = 0
    fourdigitpal = 0
   
    for x in range(10, 100): 
        if (isPalindrome(x) == True):
            twodigitpal = x
            
        for y in range(100, 1000): 
            temp = y + twodigitpal
            if (isPalindrome(y) == True and temp >= 1000 and isPalindrome(temp) == True): 
                fourdigitpal = temp
                threedigitpal = y
                print(twodigitpal, threedigitpal, fourdigitpal, 'puzzle1 iterations', y)
                break
            
        if (isPalindrome(y) == True and temp >= 1000 and isPalindrome(temp) == True):
            break    


def make_palindromes(d):
    highest = int(pow(10, d)) + 1
    half = int(pow(10, d // 2))
    result = []
    for i in range(half + 1):
        num = str(i)
        if num[0] != '0':
            if d % 2 == 0:
                palin = int(num + num[::-1])
                if palin < highest:
                    if len(str(palin)) == d:
                        result.append(palin)
            else:
                for j in range(10):
                    palin = int(num + str(j) + num[::-1])
                    if palin < highest:
                        if len(str(palin)) == d:
                            result.append(palin)
                                   
    return result


def puzzle2():
    twos = make_palindromes(2)
    threes = make_palindromes(3)
   
    for two in twos:
        count = 0
        for three in threes:
            four = two + three
            if isPalindrome(four) and four > 1000:
                print(two, three, four, 'puzzle2 iterations', count)
            count += 1


puzzle1()            
puzzle2()
