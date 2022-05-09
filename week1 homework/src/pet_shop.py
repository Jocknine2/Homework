def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(shop_name):
    return shop_name["admin"]["total_cash"]


def add_or_remove_cash(shop, additional_cash):
    shop["admin"]["total_cash"] += additional_cash


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, sales):
    shop["admin"]["pets_sold"] += sales


def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
    pets = []

    for pet_breed in shop["pets"]:
        if pet_breed["breed"] == breed:
            pets.append(breed)

    return pets


def find_pet_by_name(shop, pet_name):

    for name in shop["pets"]:
        if name["name"] == pet_name:
            return name


def remove_pet_by_name(shop, name):

    remaining_pets = []
    for pets in shop["pets"]:
        if pets["name"] != name:
            remaining_pets.append(pets)

    shop["pets"] = remaining_pets


def add_pet_to_stock(shop, new_pet):

    shop["pets"].append(new_pet)

    return shop["pets"]


def get_customer_cash(customer):

    return customer["cash"]


def remove_customer_cash(customer, amount):

    customer["cash"] -= amount


def get_customer_pet_count(count):

    return len(count["pets"])


def add_pet_to_customer(customer, pet):
    return customer["pets"].append(pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False
