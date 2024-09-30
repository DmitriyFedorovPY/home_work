values_list = [23.5, 'Баскетбол', False]
values_dict = {'a': 44, 'b': 'Хоккей', 'c': True}
values_list_2 = [54.32, 'Футбол' ]

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2)