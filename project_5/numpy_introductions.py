import numpy as np

temperatures = np.array([28.5, 21.0, 19.8, 22.1, 20.0, 17.5, 23.0])

average = np.mean(temperatures)
print(f"Average temperature: {average:.1f}°C ")
print("Days over average🔥")
for day, temperature in enumerate(temperatures, start=1):
    if temperature > average:
        print(f"Day {day}: {temperature:.1f}°C")