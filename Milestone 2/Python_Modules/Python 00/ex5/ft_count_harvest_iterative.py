def ft_count_harvest_iterative():
    y = int(input("Days until harvest: "))
    x = range(1, y + 1)
    for n in x:
        print("Day", n)
    print("Harvest time!")

ft_count_harvest_iterative()