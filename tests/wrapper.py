from OrderBook import OrderBook
from Order import Order


class MyWrapper:

    @staticmethod
    def return_order_by_list_index(order_book, i):
        return [order_book.order_book[i].id,
                order_book.order_book[i].order_type,
                order_book.order_book[i].price,
                order_book.order_book[i].volume]

    @staticmethod
    def return_orders_by_list_indexes(order_book, indexes_list):
        actual_orders = []
        for i in indexes_list:
            actual_orders.append(MyWrapper.return_order_by_list_index(order_book, i))
        return actual_orders
