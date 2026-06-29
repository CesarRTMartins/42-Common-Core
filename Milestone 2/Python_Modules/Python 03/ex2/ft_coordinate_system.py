import sys
from math import sqrt
argc = len(sys.argv)
print("=== Game Coordinate System ===")
print()

try:
    if len(sys.argv) != 7:
        raise ValueError("Invalid number of arguments")

    coords = ()
    i = 1
    while i < 7:
        nb = int(sys.argv[i])
        coords += (nb,)
        i += 1

    print("Position created:", coords[:3])

    pos = sqrt(
        (coords[3] - coords[0])**2 +
        (coords[4] - coords[1])**2 +
        (coords[5] - coords[2])**2
    )

    print(f"Distance between ({coords[3]}, {coords[4]}, "
          f"{coords[5]}) and ({coords[0]}, {coords[1]}, "
          f"{coords[2]}) {pos:.2f}")
    print()
    print("Unpacking demonstration:")
    print(f"Player at x={coords[0]}, y={coords[1]}, x={coords[2]}")
    print(f"Coordinates: X={coords[3]}, Y={coords[4]}, "
          f"Z={coords[5]}")
except ValueError:
    err_msg = "invalid literal for int() with base 10:"
    print(f"Error parsing coordinates: {err_msg} '{sys.argv[i]}'")
    print(f"Error details - Type: ValueError, Args: "
          f"({err_msg} '{sys.argv[i]}',)")
