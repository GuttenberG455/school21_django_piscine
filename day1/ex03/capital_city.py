import sys


def get_capital(state):
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
    key = states.get(state)
    if key:
        print(capital_cities.get(key))
    else:
        print("Unknown state")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_capital(sys.argv[1])
