import time


def game_events(n):
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]

    i = 0
    while i < n:
        player = players[i % 3]
        action = actions[i % 3]
        level = levels[i % 3]

        yield (i + 1, player, level, action)

        i += 1


def fibonacci(n):
    a = 0
    b = 1
    i = 0

    while i < n:
        yield a
        a, b = b, a + b
        i += 1


def primes(n):
    num = 2
    count = 0

    while count < n:
        prime = True
        i = 2

        while i < num:
            if num % i == 0:
                prime = False
                break
            i += 1

        if prime:
            yield num
            count += 1

        num += 1


print("=== Game Data Stream Processor ===")
print()
print("Processing 1000 game events...")
print()

total = 0
high_level = 0
treasure = 0
levelup = 0

start = time.time()

for event_id, player, level, action in game_events(1000):

    if event_id <= 3:
        print(f"Event {event_id}: Player {player} (level {level}) {action}")
    elif event_id == 4:
        print("...")

    total += 1

    if level >= 10:
        high_level += 1

    if action == "found treasure":
        treasure += 1

    if action == "leveled up":
        levelup += 1

end = time.time()
print()
print("=== Stream Analytics ===")
print("Total events processed:", total)
print("High-level players (10+):", high_level)
print("Treasure events:", treasure)
print("Level-up events:", levelup)
print()
print("Memory usage: Constant (streaming)")
print("Processing time:", round(end - start, 3), "seconds")
print()

print("=== Generator Demonstration ===")

print("Fibonacci sequence (first 10):", end=" ")
for x in fibonacci(10):
    print(x, end=", ")
print()

print("Prime numbers (first 5):", end=" ")
for p in primes(5):
    print(p, end=", ")
print()
