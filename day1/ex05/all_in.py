import sys


def get_value(dictionary, target):
    for key, value in dictionary.items():
        if key.upper() == target.upper():
            return value
    return None


def get_key(dictionary, target):
    for key, value in dictionary.items():
        if value.upper() == target.upper():
            return key
    return None


def print_capital_or_state(line):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    value = get_value(states, line)
    key = get_key(capital_cities, line)
    if value:
        print(f"{capital_cities.get(value)} is the capital of {get_key(states, value)}")
    elif key:
        print(f"{capital_cities.get(key)} is the capital of {get_key(states, key)}")
    else:
        print(f"{line} is neither a capital city nor a state")


def parse_arg(line):
    words = line.split(',')
    for word in words:
        word = word.strip()
        if word != '':
            print_capital_or_state(word)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        parse_arg(sys.argv[1])
