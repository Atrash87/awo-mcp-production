from pathlib import Path


DATA_DIR = Path("data")

files = [
    "angebotSchema.csv",
    "adresseSchema.csv",
    "einrichtungSchema.csv",
    "traegerSchema.csv",
]


for filename in files:
    path = DATA_DIR / filename

    print("=" * 70)
    print(filename)
    print("=" * 70)

    with open(path, "rb") as f:
        raw = f.read()

    # Find the first bytes that are outside standard ASCII.
    non_ascii_positions = [
        i for i, byte in enumerate(raw)
        if byte > 127
    ]

    if not non_ascii_positions:
        print("No non-ASCII bytes found.")
        print()
        continue

    first_position = non_ascii_positions[0]

    # Show some bytes around the first non-ASCII character.
    start = max(0, first_position - 20)
    end = min(len(raw), first_position + 30)

    print(f"First non-ASCII byte position: {first_position}")
    print()
    print("Raw bytes around it:")
    print(raw[start:end])

    print()
    print("Same bytes interpreted as UTF-8:")

    try:
        print(raw[start:end].decode("utf-8"))
    except UnicodeDecodeError as e:
        print(f"UTF-8 decoding failed: {e}")

    print()
    print("Same bytes interpreted as cp1252:")

    try:
        print(raw[start:end].decode("cp1252"))
    except UnicodeDecodeError as e:
        print(f"cp1252 decoding failed: {e}")

    print()