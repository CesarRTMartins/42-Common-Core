print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print()

print("Initiating secure vault access...")

try:
    print("Vault connection established with failsafe protocols")
    print()
    print("SECURE EXTRACTION:")

    with open("classified_data.txt", "r") as file:
        for line in file:
            print(line, end="")
    print()
    print()
    print("SECURE PRESERVATION:")

    with open("secure_archive.txt", "w") as file:
        file.write("[CLASSIFIED] New security protocols archived\n")

    print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print()

except Exception:
    print("ERROR: Vault access compromised.")

print("All vault operations completed with maximum security.")
