def water_plants(plant_list):
    print("Opening watering system")
    try:
        for n in plant_list:
            if not isinstance(n, str) or n == "":
                msg = "Error: Cannot water None - invalid plant!"
                raise ValueError(msg)
            print("Watering", n)
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("Testing with error...")
    good_list = ["tomato", ""]
    water_plants(good_list)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    lst = ["tomato", "lettuce", "carrots"]
    water_plants(lst)
    print("Watering completed successfully!")
    print()
    test_watering_system()
