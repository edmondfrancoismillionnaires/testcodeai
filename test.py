def ispair(n):
    if n%2 == 0:
        return 'pair'
    return 'impair'

def typic_branch(n):
    if n % 2 == 0:
        n = 2*n + 1
    elif n%2 == 1:
        n = 2*n
    if n % 2 == 0:
        return 0
    elif n%2 == 1:
        return 1
