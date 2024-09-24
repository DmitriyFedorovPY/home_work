numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
input_ = int(input('Введите число от 3 до 20: '))
for i in numbers:
    for j in numbers:
        if input_ % (i + j)  == 0 and j < input_ and i < input_ and j < i:
            print(j , i)



