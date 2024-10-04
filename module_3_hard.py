data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((2, 'Urban', 'Urban2', 35))
]

def total_sum(data):
    total = 0
    for item in data:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, list) or isinstance(item, tuple):
            total += total_sum(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                total += len(key)
                if isinstance(value, int):
                    total += value
                elif isinstance(value, str):
                    total += len(value)
    return total

total = total_sum(data_structure)
print(total)