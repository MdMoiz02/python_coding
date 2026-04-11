"""Given a tuple like (1, 2, (3, 4), 5), write a program to "flatten" it into a simple list: [1, 2, 3, 4, 5]."""
def flatten_tuple(tup):
    flat_list = []
    for item in tup:
        if isinstance(item, tuple):
            flat_list.extend(flatten_tuple(item))
        else:
            flat_list.append(item)
    return flat_list
