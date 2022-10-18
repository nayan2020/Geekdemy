
class Item:
    '''Details about the particular item'''
    def __init__(self, name: str, rate: int, pro_discount: float) -> None:
        self._name = name
        self._rate = rate
        self._pro_discount = pro_discount

    def get_name(self):
        return self._name

    def get_rate(self) -> int:
        return self._rate

    def get_pro_discount(self) -> float:
        return self._pro_discount


class Programme:
    def __init__(self):
        '''Store the total number of element and
        gives the required Access of the User'''
        self._container = dict()

    def add_programme(self, name: str, rate: int, pro_discount: float) -> None:
        self._container[name] = Item(name=name, rate=rate, pro_discount=pro_discount)

    def get_programme_rate(self, name: str) -> int:
        return self._container[name].get_rate()

    def get_programme_discount(self, name: str) -> int:
        return self._container[name].get_pro_discount()
