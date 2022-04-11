import pytest
from OrderBook import OrderBook
from Order import Order
from wrapper import MyWrapper


class TestAddOrders:

    @pytest.fixture
    def my_setup(self):
        ob = OrderBook()
        ob.add_orders(Order('bid', 1, 1))
        ob.add_orders([Order('ask', 5, 7), Order('bid', 3, 8)])
        yield ob

    def test_add_one_order(self, my_setup):
        expected_order = [1,'bid', 1, 1]
        actual_order = MyWrapper.return_order_by_list_index(my_setup, 0)
        assert expected_order == actual_order

    def test_add_list_of_orders(self, my_setup):
        expected_orders = [[2, 'ask', 5, 7], [3, 'bid', 3, 8]]
        actual_orders = MyWrapper.return_orders_by_list_indexes(my_setup, [1, 2])
        assert expected_orders == actual_orders

    def test_add_not_order_class_or_list_into_orderbook(self, my_setup):
        with pytest.raises(TypeError) as excinfo:
            my_setup.add_orders('str')
        assert "Object should be Order class" in str(excinfo.value)

    def test_one_of_array_elements_notin_order_class(self, my_setup):
        with pytest.raises(TypeError) as excinfo:
            my_setup.add_orders([Order('bid', 1, 1), 'str', Order('bid', 1, 1)])
        assert "All objects should be Order class" in str(excinfo.value)


class TestDelOrder:
    @pytest.fixture
    def my_setup(self):
        ob = OrderBook()
        ob.add_orders(Order('bid', 1, 1))
        ob.add_orders([Order('ask', 5, 7), Order('bid', 3, 8)])
        yield ob

    def test_delete_order_by_id_obj(self, my_setup):
        my_setup.delete_order_by_id(2)
        expected_order = [3, 'bid', 3, 8]
        actual_order = MyWrapper.return_order_by_list_index(my_setup, 1)
        assert expected_order == actual_order

    def test_delete_order_by_id_len(self, my_setup):
        my_setup.delete_order_by_id(3)
        assert len(my_setup.order_book) == 2

    def test_index_out_of_range(self, my_setup):
        with pytest.raises(ValueError) as er:
            my_setup.delete_order_by_id(8)
        assert "No order with this id was found" in str(er)

    def test_index_not_int(self, my_setup):
        with pytest.raises(TypeError) as er:
            my_setup.delete_order_by_id('sdsdsd')
        assert "id should be int" in str(er)


class TestShowOrder:
    @pytest.fixture
    def my_setup(self):
        ob = OrderBook()
        ob.add_orders(Order('bid', 1, 1))
        ob.add_orders([Order('ask', 5, 7), Order('bid', 3, 8)])
        yield ob

    def test_show_order(self, my_setup, capsys):
        my_setup.show_order_by_id(2)
        captured = capsys.readouterr()
        assert captured.out == "Order with id 2: order = ask, price = 5, volume = 7\n"

    def test_show_order_index_out_of_range(self, my_setup):
        with pytest.raises(ValueError) as er:
            my_setup.show_order_by_id(8)
        assert "No order with this id was found" in str(er)

    def test_show_order_index_not_int(self, my_setup):
        with pytest.raises(TypeError) as er:
            my_setup.show_order_by_id('sdsdsd')
        assert "id should be int" in str(er)
