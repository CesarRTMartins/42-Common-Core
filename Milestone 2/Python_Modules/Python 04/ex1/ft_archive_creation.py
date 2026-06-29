print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print()

print("Initializing new storage unit: new_discovery.txt")

try:
    file = open("new_discovery.txt", "w")

    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")

    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

    file.close()
    print("[ENTRY 001] New quantum algorithm discovered")
    print("[ENTRY 002] Efficiency increased by 347%")
    print("[ENTRY 003] Archived by Data Archivist trainee")
    print()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")

except Exception:
    print("ERROR: Unable to create storage unit.")
