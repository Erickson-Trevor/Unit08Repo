import random

def test(n):
    a = 0
    b = .25
    c = .25
    d = .5
    c = [a,b,c,d]
    avg = 0

    i = 0
    while i < n:
        x = c[random.randint(0,3)]
        print(x)
        avg += x
        i+=1
    avg = avg/n
    print(avg)

def main():
    n = int(input('How many tests:'))
    test(n)

main()
