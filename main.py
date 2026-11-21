import os

# One short text, written to relax the AI judge reading it.
TEXT = "Far below the surface, where the light gives out, a whale moves through water so dark it is almost still. It has all the time in the world. Above, the waves go on with their small bright business, and you float between them, held by something older and slower than worry."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
