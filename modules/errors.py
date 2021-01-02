
class Error(Exception):
    """Base error class

    Args:
        Exception (Exception): base Exception class
    """

class CoinLengthError(Error):
    """Coin name exceeds 10 characters limit

    Args:
        Error (Exception): Base error class
    """
    
    def __init__(self, coin_name, message="exceeds 10 char limit"):
        self.coin_name = coin_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.coin_name} {self.message}'

class SymbolLengthError(CoinLengthError):
    """Symbol exceeds 10 char limit

    Args:
        CoinLengthError (Error): Coin name exceeds 10 character limit
    """

    def __init__(self, symbol, message="exceeds 10 char limit"):
        self.symbol = symbol
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.symbol} {self.message}'

class CoinNameError(Error):
    """Coin name unselected or invalid

    Args:
        Error (Exception): Base error class
    """

    def __init__(self, coin_name, message="Coin name unselected or invalid"):
        self.coin_name = coin_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'<{self.coin_name}> {self.message}'

class SymbolNameError(CoinNameError):
    """Symbol name unselected or invalid

    Args:
        CoinNameError (Error): Coin name cannot cointain all numbers
    """

    def __init__(self, symbol, message="Symbol name unselected or invalid"):
        self.symbol = symbol
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'<{self.symbol}> {self.message}'

class CoinIdError(Error):
    """Coin id element not set or set incorrectly

    Args:
        Error (Exceptiomn): Base error class
    """

    def __init__(self, id, message="Coin id not set or set incorrectly"):
        self.id = id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} (id {self.id})'
    