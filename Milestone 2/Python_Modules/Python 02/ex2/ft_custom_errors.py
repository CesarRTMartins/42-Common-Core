class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, detail):
        super().__init__(detail)


class WaterError(PlantError):
    def __init__(self, detail):
        super().__init__(detail)


def check_plant(name, water):
    if water < 20:
        raise PlantError(f"The {name} plant is wilting!")


def check_tank(level):
    if level < 200:
        raise WaterError("Not enough water in the tank!")


def check_all_errors(name, p_water, water):
    try:
        check_plant(name, p_water)
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_tank(water)
    except GardenError as e:
        print("Caught a garden error:", e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\n")
    print("Testing PlantError...")
    try:
        check_plant("tomato", 10)
    except PlantError as e:
        print("Caught PlantError:", e)
    print("\n")
    print("Testing WaterError...")
    try:
        check_tank(20)
    except WaterError as e:
        print("Caught a WaterError:", e)
    print("\n")
    print("Testing catching all garden errors...")
    check_all_errors("Tomato", 10, 10)
    print()
    print("All custom error types work correctly!")
