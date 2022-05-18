def my_var():
    var = 42
    print(f"{var} has a type {type(var)}")
    var = str(42)
    print(f"{var} has a type {type(var)}")
    var = 'quarante-deux'
    print(f"{var} has a type {type(var)}")
    var = float(42)
    print(f"{var} has a type {type(var)}")
    var = bool(42)
    print(f"{var} has a type {type(var)}")
    var = [42]
    print(f"{var} has a type {type(var)}")
    var = {42: 42}
    print(f"{var} has a type {type(var)}")
    var = (42, )
    print(f"{var} has a type {type(var)}")
    var = set()
    print(f"{var} has a type {type(var)}")


if __name__ == '__main__':
    my_var()
