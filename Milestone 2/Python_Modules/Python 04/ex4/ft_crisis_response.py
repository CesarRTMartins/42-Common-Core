def crisis_handler(file):
    try:
        if file == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")

        if file == "lost_archive.txt":
            raise FileNotFoundError
        if file == "classified_vault.txt":
            raise PermissionError

        with open(file, "r") as f:
            content = f.read()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
            print()

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
print()

with open("standard_archive.txt", "w") as f:
    f.write("Knowledge preserved for humanity")

crisis_handler("lost_archive.txt")
crisis_handler("classified_vault.txt")
crisis_handler("standard_archive.txt")

print("All crisis scenarios handled successfully. Archives secure.")
