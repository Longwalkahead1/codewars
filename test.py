import random
moods = ["happy","sad", "energetic","lonely","hopeful"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]
for index in range(len(days)):
    mood = random.choice(moods)
    print(f"on {days[index]},I am feeling {mood}")
