import random

def headify(f):
    txt = f()
    def inner():
        return '<h1>' + txt + '</h1>'
    return inner
@headify
def greet():
    greetings = ['print("Hello")','print "Hello"','System.out.println("Hello")','console.log("Hello")']
    return random.choice(greetings)
def greet2():
    greetings = ['print("Hello")','print "Hello"','System.out.println("Hello")','console.log("Hello")']
    return random.choice(greetings)



#print(greet())
#print(greet2())

def memoize(f):
    memo = {}
    def helper(x):
        if x in memo:
            return memo[x]
        else:

    return helper
@memoize
def fibrec(n):
    return 1 if n == 0 or n == 1 else fibrec(n-1)+fibrec(n-2)

#print(fibrec(40))
fib = fibrec

print(fib(40))

def fib():
    nums = [1,1]
    def inner():
        nonlocal nums
        num[1] = num[0]+num[1]
        num[0] = num[1]
    return inner
