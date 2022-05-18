import sys


def get_key_by_value(dict: dict, value):
    for key, item in dict.items():
        if item == value:
            return key
    return None


def get_state(town):
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
    key = get_key_by_value(capital_cities, town)
    if key:
        print(get_key_by_value(states, key))
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_state(sys.argv[1])
