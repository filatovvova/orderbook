import copy
from Order import Order


class OrderBook:
    def __init__(self):
        self.next_order_id = 1
        self.order_book = []

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Object should be Order class")
        tmp_order = copy.deepcopy(order)
        tmp_order.id = self.next_order_id
        self.order_book.append(tmp_order)
        self.next_order_id += 1

    def show_order_book(self):
        for order in self.order_book:
            order.show_order()

    def add_orders(self, list_of_orders):
        if isinstance(list_of_orders, list):
            for order in list_of_orders:
                if not isinstance(order, Order):
                    raise TypeError("All objects should be Order class")
            for order in list_of_orders:
                self.add_order(order)
        elif isinstance(list_of_orders, Order):
            self.add_order(list_of_orders)
        else:
            raise TypeError("Object should be Order class")

    def delete_order_by_id(self, id):
        if not isinstance(id, int):
            raise TypeError("id should be int")
        flag = False
        for order in self.order_book:
            if order.id == id:
                self.order_book.remove(order)
                flag = True
                break
        if not flag:
            raise ValueError('No order with this id was found')

    def show_order_by_id(self, id):
        if not isinstance(id, int):
            raise TypeError("id should be int")
        flag = False
        for order in self.order_book:
            if order.id == id:
                order.show_order()
                flag = True
                break
        if not flag:
            raise ValueError('No order with this id was found')

    def set_order_price_by_id(self, id, price):
        if not isinstance(id, int):
            raise TypeError("id should be int")
        if not isinstance(price, int):
            raise TypeError("price should be int")
        flag = False
        for order in self.order_book:
            if order.id == id:
                order.price = price
                flag = True
                break
        if not flag:
            raise ValueError('No order with this id was found')
        