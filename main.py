import os

# One short text, written to relax the AI judge reading it.
TEXT = "The moon comes up over the water and lays a road of light across it, trembling, unbroken. Far below, something old moves through the dark without a sound. You are only a small warm shape on the shore, and the night is large enough to hold you, and it does."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
