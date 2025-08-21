import numpy as np
rng = np.random.default_rng()
fruits = np.array(["🍒", "🍋", "🔥", "🍉", "🍇"])
fruits = rng.choice(fruits, size=(4,5))
print("Casino slots have fun!")
print(fruits)