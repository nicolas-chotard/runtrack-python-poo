def power(x, n):
    """
    Cette fonction calcule x^n de manière récursive.
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x, n / 2)
    else:
        return x * power(x * x, (n - 1) / 2)

n = int(input("Entrez un nombre entier : "))

result = power(2, n)

print(f"2^{n} = {result}")
