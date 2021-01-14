from .errors import CoinNameError, SymbolNameError, CoinLengthError, SymbolLengthError, CoinIdError

class Coin:
    """Object for row in coin table used to manage and create coins
    """

    def __init__(self, coin='unselected', symbol='unselected', id=0):
        self.coin_name = coin
        self.symbol = symbol
        self.id = id

    def coin_name_check(self):
        if self.coin_name.isnumeric():
            raise CoinNameError(self.coin_name)
        elif len(self.coin_name) > 10:
            raise CoinLengthError(self.coin_name)
        elif self.coin_name == 'unselected':
            raise CoinNameError(self.coin_name)
        elif ' ' in self.coin_name:
            raise CoinNameError(self.coin_name)
        else:
            return 'Valid'

    def symbol_check(self):
        if self.symbol.isnumeric():
            raise SymbolNameError(self.symbol)
        elif len(self.symbol) > 10:
            raise SymbolLengthError(self.symbol)
        elif self.symbol == 'unselected':
            raise SymbolNameError(self.symbol)
        elif ' ' in self.symbol:
            raise SymbolNameError(self.symbol)
        else:
            return 'Valid'

    def id_check(self):
        if self.id == 0:
            raise CoinIdError(self.id)
        elif not isinstance(self.id,(int)):
            raise CoinIdError(self.id)
        elif len(str(self.id)) != 4:
            raise CoinIdError(self.id)
        else:
            return 'Valid'
