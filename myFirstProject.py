import os
os.system('cls||clear')

def main():

    #LEAP YEAR 

    year = int(input("Enter a year and I'll tell you if it is a leap year: "))

    is_ly = isLeapYear(year)

    if(is_ly):

        print(year,"is a leap year")

    else:

          print(year,"is not a leap year")



    #STRING REVERSE

    my_str1 = input("\nEnter a phrase and I'll show you it backwards: ")

    rev_str = reverseMyString(my_str1)

    print("Your phrase backward is:",rev_str)



    #PALINDROME CHECK

    my_str2 = input("\nEnter a phrase and I'll tell you if it is a palindrome or not: ")

    is_pal = isPalindrome(my_str2)

    if(is_pal):

        print("You entered a palindrome")

    else:

        print("You did not enter a palindrome")

    

    #PRIME CHECKER

    num1 = int(input("\nEnter a number and I'll tell you if it is prime or not: "))

    is_prime = isPrime(num1)

    if(is_prime):

        print(num1,"is prime")

    else:

        print(num1,"is not prime")

    

    #NEXT PRIME

    num2 = int(input("\nEnter a number and I'll tell you the next number that is prime: "))

    next_prime = nextPrime(num2)

    print("The next prime is",next_prime)


 #YOUR FUNCTIONS HERE

# isLeapYear function returns whether a year is a leap year or not
# A leap year is divisible by 4 but not 100, unless its divisible by 400
def isLeapYear(year):
    # checks if it is divisble by 4, such as 2020, but not 100, such as 1900, or divisible by 400, like 2000
    if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
        return True
    else:
        return False

# reverseMyString is a function that reverses one string and makes it a new string
def reverseMyString(string):
    val = len(string)
    val = val - 1
    #creates a new string that will contain the old string backwards
    newString = ""
    # loops through the whole string
    while val >= 0:
        character = ord(string[val])
        # Adds the new charactar from the old string to the new string
        newString = newString + chr(character)
        val = val - 1
    return newString

# isPalindrome uses the reverseMyString function to see is the original string and reversed string are the same
def isPalindrome(string):
    testString = reverseMyString(string)
    if testString == string:
        return True
    else:
        return False

# isPrime checks to see if a number is divisble by any number before it besides one
def isPrime(num):
    if num > 2:
        # starts at 2 because all numbers are divisible by one
        check = 2
        # loops through every single number before it
        while check < num:
            # checks to see if it is divisible
            if num % check == 0:
                return False
            check = check + 1
    # if it goes through every number before it and doesn't return false, it must be prime
    return True

# nextPrime uses isPrime to find the next highest prime number
def nextPrime(num):
    check = False
    num = num + 1
    # loop keeps adding one to number until isPrime returns true, then returns the prime number
    while check == False:
        if isPrime(num) == True:
            return num
        else:
            num = num + 1
        
# calls the main function
main()
