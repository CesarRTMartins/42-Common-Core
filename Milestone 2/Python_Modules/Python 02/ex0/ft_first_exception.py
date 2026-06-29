def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        temp = temp_str
        print(f"Error: '{temp}' is not a valid number")
        return None
    if temp >= 0 and temp <= 40:
        return temp
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")


def test_temperature_input():
    tests = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")
    print()
    for n in tests:
        print("Testing temperature:", n)
        result = check_temperature(n)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")
            print("\n")
        else:
            print("\n")
        print("All tests complete - program didn't crash")


if __name__ == "__main__":
    test_temperature_input()
