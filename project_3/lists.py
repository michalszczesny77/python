animals = ["dog", "cat", "crocodile"]

for x, animal in enumerate(animals):
    print(x, animal)
print("")

dictionary = {
    "Poland": "Warsaw",
    "Germany": "Berlin"
} 

for key, value in dictionary.items():
    print(f"{key}-{value}")