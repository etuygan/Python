n = int(raw_input("enter a number: "))

def factorial_iter(n):
    if n == 0:
        return 1
    else:
        return (n * factorial_iter(n-1))

print factorial_iter(n)

def summ(n):
    toplam = 0
    for i in range(n+1):
        toplam = toplam + i
    return toplam


print summ(4)

n = int(raw_input("enter a number: "))

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2) 

print fibonacci_rec(n)


a = int(raw_input("enter a number for a: "))
b = int(raw_input("enter a number for b: "))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,(a%b))

print gcd(a,b)

m = int(raw_input("enter a number to sum: "))

def summ(m):
    if m == 0:
        return 0
    else:
        return (m + summ(m-1))

print summ(m)
