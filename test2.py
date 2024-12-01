import random
times = ["morninings", "afternoon", "evening"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]
moods = ["happy", "sad", "angry", "eager", "depressed", "lonely", "content"]
for index in range(len(days)):
    mood= random.choice(moods)
    for point in range(len(times)):
        print(f"on {days[index]} {times[point]}, I was {mood}")
        
