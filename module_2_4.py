numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
count = 0
for i in numbers:
    for j in range(1,i+1):
        if i % j  == 0:
            count += 1
    if count == 2:
        primes.append(i)
    count = 0
for i in numbers:
    for j in range(1,i+1):
        if i % j  == 0:
            count += 1
    if count != 2 and i != 1:
        not_primes.append(i)
    count = 0
print(f'primes: {primes}')
print(f'not primes: {not_primes}')
