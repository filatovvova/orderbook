import pytest
from Order import Order
from wrapper import MyWrapper


class TestOrder:

    def test_bid_order(self):
        assert MyWrapper.return_order_as_list(Order('bid', 1, 1)) == [None, 'bid', 1, 1]

    def test_ask_order(self):
        assert MyWrapper.return_order_as_list(Order('ask', 2, 5)) == [None, 'ask', 2, 5]

    def test_type_not_in_list(self):
        with pytest.raises(AttributeError) as er:
            Order('bit', 1, 1)
        assert "order_type should be 'bid' or 'ask'" in str(er.value)

    def test_price_not_int(self):
        with pytest.raises(TypeError) as er:
            Order('bid', 1.1, 1)
        assert "price should be int" in str(er.value)

    def test_volume_not_int(self):
        with pytest.raises(TypeError) as er:
            Order('bid', 1, 'dgh')
        assert "volume should be int" in str(er.value)
