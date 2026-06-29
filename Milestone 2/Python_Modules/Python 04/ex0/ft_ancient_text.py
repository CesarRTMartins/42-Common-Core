print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print()
print("Accessing Storage Vault: ancient_fragment.txt")

try:
    print("Connection established...")
    print()
    print("RECOVERED DATA:")
    with open("ancient_fragment.txt") as file_handle:
        for line in file_handle:
            print(line, end="")
    print('\n')
    print("Data recovery complete. Storage unit disconnected.")
except Exception:
    print("ERROR: Storage vault not found. Run data generator first.")
