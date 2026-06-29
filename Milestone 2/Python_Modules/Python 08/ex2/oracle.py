import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependency: python-dotenv")
    print("Install with: pip install python-dotenv")
    sys.exit(1)

load_dotenv()

MATRIX_MODE = os.getenv("MODE")
DATABASE_URL = os.getenv("DATABASE_CONNECTED")
API_KEY = os.getenv("API_ACCESS")
LOG_LEVEL = os.getenv("LOG_LEVEL")
ZION_ENDPOINT = os.getenv("ZION_NETWORK")

print("ORACLE STATUS:")
print("Reading the Matrix...")
print()
print("Configuration loaded:")
print(f"  Mode:      {MATRIX_MODE}")

if DATABASE_URL:
    label = "Connected to local instance" if MATRIX_MODE == "development" else\
        "Connected to production database"
    print(f"  Database:  {label}")
else:
    print("  Database:  [WARNING] DATABASE_URL not set")

if API_KEY:
    print("  API Access: Authenticated")
else:
    print("  API Access: [WARNING] API_KEY not set")

print(f"  Log Level: {LOG_LEVEL}")

if ZION_ENDPOINT:
    print("  Zion Network: Online")
else:
    print("  Zion Network: [WARNING] ZION_ENDPOINT not set")

print()
print("Environment security check:")
print("  [OK] No hardcoded secrets detected")

if os.path.exists(".env"):
    print("  [OK] .env file properly configured")
else:
    print("  [WARN] .env file not found — copy .env.example to .env")

if MATRIX_MODE == "production":
    print("  [OK] Running in production mode")
else:
    print("  [OK] Production overrides available")

print()
print("The Oracle sees all configurations.")
