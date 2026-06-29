def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print(seed, "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(seed, "seeds:", quantity, unit, "grams total")
    elif unit == "area":
        print(seed, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")

ft_seed_inventory("tomato", 5, "packets")
ft_seed_inventory("carrot", 200, "grams")  
ft_seed_inventory("lettuce", 10, "area")   