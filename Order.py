import const


class Order:
    def __init__(self, order_type, price, volume):
        if order_type not in const.order_type_list:
            raise AttributeError("order_type should be 'bid' or 'ask")
        if not isinstance(price, int):
            raise TypeError("price should be int")
        if not isinstance(volume, int):
            raise TypeError("volume should be int")
        self.id = None
        self.order_type = order_type
        self.price = price
        self.volume = volume

    def show_order(self):
        print(f'Order with id {self.id}: order = {self.order_type}, price = {self.price}, volume = {self.volume}')
