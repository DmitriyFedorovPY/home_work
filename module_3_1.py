calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    long = len(string)
    up = (string.upper())
    down = (string.lower())
    tuple = (long, up, down)
    count_calls()
    print(tuple)

def is_contains(string, list_to_search):
    down_1 = string.lower()
    for i in list_to_search:
        down_2 = i.lower()
    res = down_1 in down_2
    count_calls()
    print(res)

string_info('Привет')
string_info('Я я е Ко Ко ДжаМбо')
is_contains('Urban', ['kek','urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)





