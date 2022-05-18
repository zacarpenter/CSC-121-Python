def get_milkshake():
    # loop to ask the user for a flavor choice
    while True:
        # try block validates the user input an available flavor
        try:
            flavor = input("What flavor would you like? ")
            # available flavor breaks from the loop
            if flavor == 'vanilla' or flavor == 'chocolate' or flavor == 'strawberry':
                break
            else:
                print("There are only 3 flavors available: Vanilla, Chocolate, and Strawberry. Please choose again.")
        # if the user choice is not an available flavor, continue looping
        except:
            continue
    return print("You chose " + flavor)

get_milkshake()
