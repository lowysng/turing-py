from random import random, randint

def get_states(n):
    return ['q' + str(x) for x in list(range(1, n + 1))]

def generate_random_string(alphabet):
    length = randint(1, 8)
    string = ''
    for i in range(length):
        string += alphabet[randint(0, len(alphabet) - 1)]
    return string