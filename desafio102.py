from math import factorial
def fatorial(num, show):
    if show == bool(False):
        return factorial(num)
    else:
        fatorialnum = factorial(num)
        c = num
        while c > 0:
            print(f'{num}', end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            c -= 1
            num -= 1
        return fatorialnum

print(fatorial(5, show=True))