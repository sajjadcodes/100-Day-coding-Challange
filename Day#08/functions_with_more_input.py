
# Fuctions with more than 1 inut

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Jack Bauer", "Nowhere")

# changing orders: positional arguement. Default way
#order matters
greet_with("nowhere", "jack Bauer")

#keyword Argument: order does not matter

greet_with( location="islamabad" ,name="Sajjad")