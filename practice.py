# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def makes10(x, y):
    dif_1 = abs(x - y);
    dif_2 = abs(y - x);
    
    if (dif_1 == 10 or dif_2 == 10 or x + y == 10):
        return True
    
def finalcost(cost, tip):
    tipAmount = (tip / 100) * cost;
    return (cost + tipAmount)

def gradeCalculator(grade):
    gradeLetter = "";
    if (grade > 90):
        gradeLetter = "A"
    elif (grade >= 80 and grade <= 90):
        gradeLetter = "B"
    elif (grade >= 70 and grade <= 80):
        gradeLetter = "C"
    elif (grade >= 60 and grade <= 70):
        gradeLetter = "D"
    elif (grade < 60):
        gradeLetter = "R"
        
    print(gradeLetter)
    
def printEvensToN(n):
    sum = 0
    for i in range (0,n,2):
        sum += i
    print(sum)
    
def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)

#### PROBLEM 1 ####

# Given an integer n, return True if n is even and return False otherwise. 
# Hint: use the % operator.
def isEven(n):
    if (n % 2 == 0):
        return True
    else:
        return False


#### PROBLEM 2 ####

# Given an integer n, return the ones-digit of n,
# i.e. the first digit of n from the right.
def onesDigit(n):
    return abs(n) % 10

# Given an integer n, return the tens-digit of n,
# i.e. the 2nd digit of n from the right.
def tensDigit(n):
    n = abs(n) % 100
    onesDigit = n % 10
    return (n - onesDigit) / 10

# Given an integer n and k, return the (k+1)'th digit of n from the right.
# So k = 0 refers to the ones-digit, k = 1 refers to the tens-digit, etc.
# You can assume k is non-negative.
def getKthDigit(n, k):
    modNum = 10 ** (k + 1) 
    n = abs(n) % modNum
    
    if (modNum > 10):
        modNum = modNum / 10
        digitBefore = n % modNum
        n = n - digitBefore
        n = n / modNum
        
    return n

# Given integers n, k and d, replace the kthDigit of n with d.
# You can assume k is non-negative, and d is an integer between 0 and 9.
def setKthDigit(n, k, d):
    modNum = 10 ** (k + 1) 
    tempNum = abs(n) % modNum
    
    if (modNum > 10):
        modNum = modNum / 10 
        d = d * modNum
        lowerDigits = tempNum % modNum
    else:
        lowerDigits = 0
        
    tempNum = abs(n) - tempNum
    tempNum += d
    tempNum += lowerDigits
    
    if (n < 0):
        tempNum = 0 - tempNum
        return tempNum
    else:
        return tempNum

#### PROBLEM 3 ####

# Given a float n, round it to the nearest odd integer.
# In case of a tie, round down.
def nearestOdd(n):
    decimal = n % 1
    wholeNum = n - decimal
    modNum = wholeNum % 2
    if (modNum == 1):
        return wholeNum
    if (modNum == 0):
        if (decimal == 0):
            return wholeNum - 1
        else:
            return wholeNum + 1

#### PROBLEM 4 ####

# See here for the description of the function:
# http://www.kosbie.net/cmu/spring-16/15-112/notes/hw1.html
def lineIntersection(m1, b1, m2, b2):
    # helper fn for threeLinesArea
    #y = mx + b
    if (m1 == m2):
        return None
    bNum = b1 - b2
    mNum= m2 - m1
    return (bNum / mNum)
    
def distance(x1, y1, x2, y2):
    # helper fn for threeLinesArea
    xNum = (x2 - x1) ** 2
    yNum = (y2 - y1) ** 2
    return math.sqrt(xNum + yNum)

def triangleArea(s1, s2, s3):
    # helper fn for threeLinesArea
    semiPerimeter = .5 * (s1 + s2 + s3)
    return math.sqrt(semiPerimeter * (semiPerimeter - s1) * (semiPerimeter - s2) * (semiPerimeter - s3))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    intersection1 = lineIntersection(m1, b1, m2, b2)
    intersection2 = lineIntersection(m2, b2, m3, b3)
    intersection3 = lineIntersection(m3, b3, m1, b1)
    distance1 = distance(intersection1, (m1*intersection1 + b1), intersection2, (m2*intersection2 + b2))
    distance2 = distance(intersection2, (m2*intersection2 + b2), intersection3, (m3*intersection3 + b3))
    distance3 = distance(intersection3, (m3*intersection3 + b3), intersection1, (m1*intersection1 + b1))
    return triangleArea(distance1, distance2, distance3)


#### PROBLEM 5 ####

# Given an integer n, return the number of digits of n.
# NOTE: you must use a loop to get credit.
def numberLength(n):
    lengthNum = 0
    i = 1
    while (abs(n) % i < abs(n)):
        if (lengthNum < abs(n)):
            lengthNum += 1
            i *= 10
    
    if (lengthNum == 0):
        lengthNum = 1
        
    return lengthNum


#### PROBLEM 6 ####

# Definition: For a positive integer n, n factorial, denoted n!,
# is the product n*(n-1)*(n-2)*...*1. If n = 0, then define 0! as 1.
# Given an integer n (which you can assume is non-negative),
# return n! (n factorial). NOTE: you may not call math.factorial!
# That would be too easy. You must use a loop to get credit.
def factorial(n):
    if (n == 0):
        return 1
    nNum = n
    factorial = 1
    while (nNum > 1):
        factorial *= nNum
        nNum = nNum - 1
        
    return factorial


#### PROBLEM 7 ####

# Given a string s, return a new string, t, that contains each letter 
# of s twice. For example, if doubleLetter is given the string 'apple', 
# it will return 'aappppllee'
def doubleLetter(s):
    string = ""
    num = 0
    while (num < len(s)):
        string = string + s[num] + s[num]
        num += 1
    return string



# If you have written the functions correctly, you should not get any errors
# when you run this file, i.e., you should pass all the tests below.


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

import math

def testIsEven():
    print("Testing isEven()...", end="")
    assert(isEven(0))
    assert(not isEven(1))
    assert(isEven(2))
    assert(not isEven(3))
    assert(isEven(4))
    assert(not isEven(-1))
    assert(isEven(-2))
    assert(not isEven(-3))
    assert(isEven(-4))
    assert(isEven(123456))
    print("Passed.")

def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert(onesDigit(0) == 0)
    assert(onesDigit(789) == 9)
    assert(onesDigit(7) == 7)
    assert(onesDigit(-1234) == 4)
    assert(onesDigit(-3) == 3)
    print("Passed.")

def testTensDigit():
    print("Testing tensDigit()...", end="")
    assert(tensDigit(0) == 0)
    assert(tensDigit(1) == 0)
    assert(tensDigit(10) == 1)
    assert(tensDigit(21) == 2)
    assert(tensDigit(-1234) == 3)
    assert(tensDigit(-3) == 0)
    assert(tensDigit(-10) == 1)
    print("Passed.")

def testGetKthDigit():
    print("Testing getKthDigit()...", end="")
    assert(getKthDigit(0,0) == 0)
    assert(getKthDigit(789, 0) == 9)
    assert(getKthDigit(789, 1) == 8)
    assert(getKthDigit(789, 2) == 7)
    assert(getKthDigit(789, 3) == 0)
    assert(getKthDigit(-1234, 3) == 1)
    assert(getKthDigit(-3, 1) == 0)
    print("Passed.")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    assert(setKthDigit(777, 2, 7) == 777)
    assert(setKthDigit(-468, 1, 5) == -458)
    print("Passed.")

def testNearestOdd():
    print("Testing nearestOdd()...", end="")
    assert(nearestOdd(0) == -1)
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print("Passed.")

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed.")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed.")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed.")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed.")

def testNumberLength():
    print("Testing numberLength()...", end="")
    assert(numberLength(0) == 1)
    assert(numberLength(1) == 1)
    assert(numberLength(9) == 1)
    assert(numberLength(10) == 2)
    assert(numberLength(1001) == 4)
    assert(numberLength(999) == 3)
    assert(numberLength(-1) == 1)
    assert(numberLength(-123) == 3)
    assert(numberLength(-123456789) == 9)
    print("Passed.")

def testFactorial():
    print("Testing factorial()...", end="")
    assert(factorial(0) == math.factorial(0))
    assert(factorial(1) == math.factorial(1))
    assert(factorial(2) == math.factorial(2))
    assert(factorial(3) == math.factorial(3))
    assert(factorial(4) == math.factorial(4))
    assert(factorial(5) == math.factorial(5))
    assert(factorial(10) == math.factorial(10))
    print("Passed.")

def testDoubleLetter():
    print("Testing doubleLetter()...", end="")
    assert(doubleLetter("apple") == "aappppllee")
    assert(doubleLetter("test") == "tteesstt")
    assert(doubleLetter("12.34") == "1122..3344")
    assert(doubleLetter("") == "")
    print("Passed.")

def testAll():
    testIsEven()
    testOnesDigit()
    testTensDigit()
    testGetKthDigit()
    testSetKthDigit()
    testNearestOdd()
    testLineIntersection()
    testDistance()
    testTriangleArea()
    testThreeLinesArea()
    testNumberLength()
    testFactorial()
    testDoubleLetter()
    
testAll()