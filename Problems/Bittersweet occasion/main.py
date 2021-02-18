# finish the function
def find_the_parent(child):
    if issubclass(child, Drinks):
        print(Drinks.__name__)

    if issubclass(child, Pastry):
        print(Pastry.__name__)

    if issubclass(child, Sweets):
        print(Sweets.__name__)
