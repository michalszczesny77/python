def greetings(name):
    print(f"Hi, welcome in hotel {name}!")

def add(x, y):
    return x + y

def price_converter(price, tax = 2, discount = 0.9 ):
    return (price + tax) * discount


greetings("Michal")
print(add(3, 5))
print(price_converter(100)) 