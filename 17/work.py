def prob5loop():
    primes = [2]
    for i in range(3,101,2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def prob5comp():
    primes = [x for x in [range(3,101,2)]]

def prob1loop(n):
    output = []
    for i in range(0, 2 * n, 2):
        output.append(str(i) * 2)
    return output

def prob1comp(n):
    return [str(i) * 2 for i in range(0, 2 * n, 2)]

def prob2loop(n):
    output = []
    for i in range(n):
        output.append(7 + i * 10)
    return output

def prob2comp(n):
    return [7 + i * 10 for i in range(n)]

def prob4loop():
    primes = [2]


# def prob5comp():
#     primes = [x for x in range(2,101) if ]
#     return (primes)

# print(prob1loop(5))
# print(prob1comp(5))
print(prob5loop())
print(prob5comp())
# print (prob5loop())
# print (prob5comp())
