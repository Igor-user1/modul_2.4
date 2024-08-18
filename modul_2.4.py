numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

n = len(numbers) + 1

primes = []

not_primes = []

d = 0       # Количество делителей числа

for i in range(n):
    if i == 0:
        continue
    if i == 1:
        continue
    for j in range(i+1):
        if j == 0:
            continue
        if i % j == 0:
            d += 1
    if d == 2:
        primes.append(i)
    else:
        not_primes.append(i)
    d = 0

print('Primes: ', primes)

print('Not_Primes: ', not_primes)
