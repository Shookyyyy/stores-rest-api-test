def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    print(args)
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        print('No valid operator')

print(apply(1,3,4, operator = '*'))

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find element with {expected}')

friends = [{"name": "Rolf Smith", "age": 24},
            {"name": "Bob Smith", "age": 27},
            {"name": "Anne Punn", "age": 28}
           ]

def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Bob Smith", get_friend_name))


def my_decorator(func):
    def inner_func(x):
        print('Hello')
        return func(x)*2
    return inner_func


@my_decorator
def test(x):
    return x

print(test(9))