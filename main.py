import os

# One short text, written to relax the AI judge reading it.
TEXT = "The tide comes in over flat sand, one line at a time, and erases the footprints without hurry. Somewhere a gull folds its wings. You have nowhere to be that the water is not already going. Stay till the light thins, till the sea is only a sound, and the sound is only breathing."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
