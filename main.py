from OrderBook import OrderBook
from Order import Order

order1 = Order('bid', 1, 1)
order2 = Order('ask', 2, 3)
order1.show_order()
order2.show_order()

order_book = OrderBook()
order_book.add_order(order1)
order_book.add_order(order2)
order_book.show_order_book()

order_book.add_order(order1)
order_book.add_order(order2)
order_book.show_order_book()

try:
    order3 = Order('pampam', 2, 3)
except AttributeError as er:
    print(er)

try:
    order4 = Order('bid', 2.2, 3)
except TypeError as er:
    print(er)

try:
    order5 = Order('bit', 2, 'sdasdasd')
except AttributeError as er:
    print(er)
except TypeError as er:
    print(er)
try:
    order_book.add_order('assd')
except TypeError as er:
    print(er)

order_book.add_orders([order1, order2])

order_book.show_order_book()

try:
    order_book.add_orders([order1, '23', order2])
except TypeError as er:
    print(er)

try:
    order_book.add_orders('23')
except TypeError as er:
    print(er)

try:
    order_book.add_orders([])
except TypeError as er:
    print(er)

order_book.show_order_book()

order_book.delete_order_by_id(5)
order_book.show_order_book()

try:
    order_book.delete_order_by_id(5)
except (ValueError, TypeError) as er:
    print(er)

order_book.show_order_book()

order_book.show_order_by_id(1)
try:
    order_book.show_order_by_id(5)
except (ValueError, TypeError) as er:
    print(er)

print(len(order_book.order_book))