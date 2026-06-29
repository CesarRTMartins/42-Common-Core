def garden_operations(case):
    if case == 1:
        number = int("abc")
        number = number
    elif case == 2:
        result = 10 / 0
        result = result
    elif case == 3:
        file = open("non_existent_file.txt", "r")
        file = file
    elif case == 4:
        plants = {"rose": 5, "tulip": 3}
        print(plants["sunflower"])


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("\n")
    print("Testing ValueError...")
    try:
        garden_operations(1)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print("\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations(2)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print("\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations(3)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print("\n")
    print("Testing KeyError...")
    try:
        garden_operations(4)
    except KeyError:
        print(r"Caught KeyError: 'missing\_plant'")
        print("\n")
    print("Testing multiple errors together...")
    try:
        garden_operations(1)
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
        print("\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
