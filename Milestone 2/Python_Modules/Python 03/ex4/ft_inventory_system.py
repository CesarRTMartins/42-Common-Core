import sys
print("=== Inventory System Analysis ===")

argc = len(sys.argv)
inventory = dict()

i = 1
while i < len(sys.argv):
    arg = sys.argv[i]

    name = ""
    qty = ""
    found = False

    for c in arg:
        if c == ":":
            found = True
        elif not found:
            name += c
        else:
            qty += c

    inventory.update({name: int(qty)})
    i += 1

total_items = 0
for v in inventory.values():
    total_items += v

print("Total items in inventory:", total_items)
print("Unique item types:", len(inventory))
print()

print("=== Current Inventory ===")

for k, v in inventory.items():
    percent = (v / total_items) * 100
    print(k + ":", v, "units (" + str(round(percent, 1)) + "%)")
print()

print("=== Inventory Statistics ===")

most_item = None
least_item = None
most_qty = -1
least_qty = 999999

for k, v in inventory.items():
    if v > most_qty:
        most_qty = v
        most_item = k
    if v < least_qty:
        least_qty = v
        least_item = k

print("Most abundant:", most_item, "(" + str(most_qty) + " units)")
print("Least abundant:", least_item, "(" + str(least_qty) + " units)")
print()

print("=== Item Categories ===")

moderate = dict()
scarce = dict()

for k, v in inventory.items():
    if v >= 5:
        moderate.update({k: v})
    else:
        scarce.update({k: v})

print("Moderate:", moderate)
print("Scarce:", scarce)
print()


print("=== Management Suggestions ===")

print("Restock needed:", end=" ")
first = True

for k, v in inventory.items():
    if v <= 1:
        if not first:
            print(",", end=" ")
        print(k, end="")
        first = False
print()
print()


print("=== Dictionary Properties Demo ===")

print("Dictionary keys:", end=" ")
for k in inventory.keys():
    print(k, end=", ")
print()

print("Dictionary values:", end=" ")
for v in inventory.values():
    print(v, end=", ")
print()

print("Sample lookup - 'sword' in inventory:", "sword" in inventory)
