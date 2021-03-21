# ENGI-E1006-GROUP-P3

**ENGI E1006 - Intro to Computing for Engineers & Applied Scientists**

**Group Exercise Set 3**

Do not use Python modules other than those explicitly mentioned. 

Unlike the take-home projects, the group exercises are intended to be worked on your assigned groups on repl.it. You can work with your group during Thursday class and you are welcome to continue in your own time. If you do not complete these problems during class, you must complete them at another time (either with your group or individually).

**Groups should upload a single version of their solutions.**

Comments in Python start with with a "# ..." 

Upload the following four files to Courseworks:

problem1_2_3.py
problem4.py

**Problem 1 (20 pts)
(problem 1, 2 and 3 should be in the same file problem1_2_3.py)**

Write a function isPalindrome(x) that takes in a positive integer x  and returns True if x is a palindromic number and False otherwise. A palindromic number is one that has an identical sequence of digits when read from left-to-right or from right-to-left, for example 5, 22, 535, 1221 are all palindromic numbers.

**Problem 2 (continuation of problem 1, 20 pts):
(problem 1, 2 and 3 should be in the same file problem1_2_3.py)**

Consider the following puzzle: There are  three hidden palindromic number. The first one is two digits long, the second one is three digits long. The third one is 4 digits long and is the sum of the previous two.

Write a function puzzle1() that compute the three numbers and then prints them. Your function does not need any parameters and can return None.

Use the isPalindrome() function to check all combinations of 2 and 3 digit numbers, as well as their sum. 

How many iterations does the inner-most loop take?  (answer in a comment at the beginning of the file)

**Problem 3 (continuation of problem 2, 20pts):
(problem 1, 2 and 3 should be in the same file problem1_2_3.py)**

Write a function make_palindromes(d) that returns a list of all palindromes with d digits. You should not iterate through all possible d-digit numbers and then check if the number is a palindrome. Instead, create all numbers with d//2 digits and then mirror the result to produce a palindrome. A small variation is needed if d is odd.

Then write a new function puzzle2() that solves the puzzle from problem 2. Instead of trying all possible combinations of numbers and using isPalindrome, use make_palindromes to obtain 2 and 3 digit palindromes. How many iterations through the inner-most loop does this version take? (answer in a comment at the beginning of the file)  

**Problem 4 (40 pts)**

In the game Hangman, the computer selects a random word that the player must guess. Instead of guessing the entire word at once, the player guesses individual letters. After each guess, the computer reveals where in the word the guessed letters appear. The computer counts how often the player guesses a letter that does not appear in the word. If the player gets more than 5 guesses wrong, the player loses. If the player uncovers all letters in the word, she wins.

Write a Python program that plays Hangman:

To guess the word, your program should read in the file dictionary.txtPreview the document and store the words in a list (we will discuss how to read files in the week of Feb 22). Then it should randomly select one word from the list.

In the main game loop, the player should make repeated guesses for letters. If the letter appears in the word, the program should print out the word with the letters uncovered. For example, if the word is college, and the user guesses “e” as the first letter, the output should be

    _ _ _ _ e _ e 
    If the player then guesses “l” in the next turn, the output should be

    _ _ l l e _ e 
    Think about how can you store the letters that have already been guessed? How do you display the word with these letters uncovered?

Save your program in a file problem4.py. 
