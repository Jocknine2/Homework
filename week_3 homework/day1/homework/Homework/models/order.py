from datetime import date


class Order:
    def __init__(self, customer, food_order, description, quantity, order_number):
        self.customer = customer
        self.food_order = food_order
        self.description = description
        self.quantity = quantity
        self.date = "18th May"
        self.order_number = order_number
