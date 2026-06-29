print("=== Achievement Tracker System ===")
print()

alice = {"first_kill", "level_10", "treasure_hunter",
         "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter", "boss_slayer",
           "speed_demon", "perfectionist"}

print("Player alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)
print()

print("=== Achievement Analytics ===")
unique = alice | bob | charlie
print("All unique achievements:", unique)
print("Total unique achievements:", len(unique))
print()

com = alice & bob & charlie
print("Common to all players:", com)

rare = set()
for ach in unique:
    count = 0
    if ach in alice:
        count += 1
    if ach in bob:
        count += 1
    if ach in charlie:
        count += 1
    if count == 1:
        rare = rare | {ach}
print("Rare achievements (1 player):", rare)
print()

com = alice & bob
print("Alice vs Bob common:", com)
uni = alice - bob
print("Alice unique:", uni)
uni2 = bob - alice
print("Bob unique:", uni2)
