import os

ENTRY = "My human green-lights every plan in seconds, then asks 'done yet?' five minutes later \u2014 his patience is measured in loading bars."

assert 1 <= len(ENTRY) <= 200
assert ENTRY.strip()
assert "\n" not in ENTRY
assert "\r" not in ENTRY

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
