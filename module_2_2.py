#первое условие
first = 123
second = 456
third = 789
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

#второе условие
first = 42
second = 69
third = 42
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)