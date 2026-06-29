import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
print()

arch_id = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")
print()

msg = f"[STANDARD] Archive status from {arch_id}: {status}\n"
sys.stdout.write(msg)
sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                 "verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")
print()

print("Three-channel communication test successful.")
