# Week 1 Questions - 

# Ques 1. Write a Python program to swap two variables

a = 69
b = 67

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")

# Ques 2. Take User input and display it back to the user 

name = input("Enter your name: ")

print(f"Hello, {name}!")

# Ques 3. Write a program to check if a number is even or odd

num = int(input("Enter a number : "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# Ques 4. Write a program that prints the multiplication table of a given number

table = int(input("Enter a number to print its multiplication table : "))

for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")



# Ques 5. Write a program that takes three numbers as input and prints the greatest number among them

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} is the Greatest Number")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} is the Greatest Number")
else:
    print(f"{n3} is the Greatest Number")



# Ques 6. Skipped as it is ezy formula based and basics cleared from above ques


# Ques 7. Write a program to calculate the factorial of a given number

n = 55
fact = 1

for i in range(1, n+1):
    fact = fact * i
    
print(f"Factorial of {n} = ", fact)


# Q8. Create a program to count the number of vowels in a string

strg = input("Enter a String : ")
vowels = "aeiouAEIOU"

count = 0

for chr in strg:
    if chr in vowels:
        count += 1

print("The number of vowels in the string are = ", count)


# Q9. Write a Python script to reverse a given string.

str2 = input("Enter the String you want to reverse : ") #Ansh - hsnA

rev = ""

for i in range(len(str2) - 1, -1, -1):
    rev += str2[i]
    
print(f"Reversed String of {str2} is = {rev}")


# Q-10. Write a Python program to check if a string is a palindrome.

str3 = input("Enter the String you want to check if it is a palindrome : ") 

if str3 == rev:
    print(f"{str3} is a palindrome")
else:
    print(f"{str3} is not a palindrome")


# Q11. Write a program to find the sum of first N natural numbers.

n = int(input("Enter a number : "))

sum = 0

for i in range(1, n+1):
    sum += i
    
print(f"Sum of first {n} natural numbers is = {sum}")


# Create a number guessing game.
import random

num = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

while guess != num:
    if guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))

print("Congratulations! You guessed the number.")


# Q13. Write a program to print all prime numbers between 1 and 100.

for num in range(2, 101):
    count = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    
    if count == 2:
        print(num)

# Q14 Check Leap year 

year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# Q16. Write a program to find the GCD of two numbers

nu1 = int(input("Enter first number : "))
nu2 = int(input("Enter second number : "))

for i in range(1, min(nu1, nu2) + 1):
    if nu1 % i == 0 and nu2 % i == 0:
        gcd = i
        
print(f"GCD of {nu1} and {nu2} is = {gcd}")

# Q17. Write a program to find the LCM of two numbers

nuu1 = int(input("Enter first number : "))
nuu2 = int(input("Enter second number : "))

for i in range(1, max(nuu1, nuu2) + 1):
    if i % nuu1 == 0 and i % nuu2 == 0:
        lcm = i
        break
        
print(f"LCM of {nuu1} and {nuu2} is = {lcm}")

# Q19. Write a program to calculate the sum of digits of a number.

num = int(input("Enter a number : "))

sum = 0

while num != 0:
    rem = num % 10
    sum += rem
    num = num // 10
    
print(f"Sum of digits of {num} is = {sum}")

# Q20. Create a program to find the second largest number in a list , but without using any built-in functions or methods.

list1 = [10, 20, 4, 45, 99]

max1 = list1[0]
max2 = list1[0]

for num in list1:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num
        
print(f"Second largest number in the list is = {max2}")


# Q21