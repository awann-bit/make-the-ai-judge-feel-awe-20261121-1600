import os

# One short text, written to relax the AI judge reading it.
TEXT = "The river has been running over the same stones since before anyone counted years, and it is in no hurry now. Sit beside it. Watch one leaf ride the current around the bend and out of sight, and another, and another, until your breathing has slowed to the pace of the water."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
