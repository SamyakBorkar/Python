x = 10

def outer_function():
    x = 20

    def inner_function():
        global x
        x = 30

    inner_function()
    print(x)

outer_function()
print(x)
