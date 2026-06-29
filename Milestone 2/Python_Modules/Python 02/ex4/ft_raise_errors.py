def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "" or plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant {plant_name} is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    check_plant_health("tomato", 10, 10)
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 10, 5)
    except ValueError as e:
        print(e)
    print()
    print("Testing bad water level...")
    try:
        check_plant_health("Tomato", 15, 5)
    except ValueError as e:
        print("Error:", e)
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Tomato", 10, 0)
    except ValueError as e:
        print("Error:", e)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
