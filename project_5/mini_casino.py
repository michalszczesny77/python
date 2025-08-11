import numpy as np
rng = np.random.default_rng()
fruits = np.array(["💥", "🍒"])
fruits = rng.choice(fruits, size=(3,3))
print("Casino slots have fun!")
print(fruits)