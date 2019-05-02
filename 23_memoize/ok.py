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
    memo = {0:0,1:1,2:1}
    def helper(x):
        if x not in memo:
            memo[x]=f(x)
        return memo[x]
    return helper
@memoize
def fibrec(n):
    return fibrec(n-1)+fibrec(n-2)

#print(fibrec(40))
fib = fibrec
print(fib(40))
