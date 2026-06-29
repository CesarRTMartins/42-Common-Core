def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def count(y):
        if (y > 0):
            count(y - 1)
            print("Day", y)
        if (y == x):
            print("Harvest time!")
        else:
            return (0)
    count(x)

ft_count_harvest_recursive()