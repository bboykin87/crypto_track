import pytest
from ..coin import Coin
from ..errors import CoinNameError, SymbolNameError, CoinLengthError, SymbolLengthError, CoinIdError

def test_coin_name_check():

    crypto = Coin('Bitcoin', 'BTC')

    assert crypto.coin_name_check() == 'Valid'

    crypto = Coin('Bitcoin2', 'BTC2')
    assert crypto.coin_name_check() =='Valid'

    crypto = Coin('unselected', 'BTC')
    with pytest.raises(CoinNameError):
        crypto.coin_name_check()

    crypto = Coin('12345', 'NUM')
    with pytest.raises(CoinNameError):
        crypto.coin_name_check()

    crypto = Coin('12345678901', 'NUM')
    with pytest.raises(CoinNameError):
        crypto.coin_name_check()

    crypto = Coin('sdnetsvafee', 'COIN')
    with pytest.raises(CoinLengthError):
        crypto.coin_name_check()

def test_symbol_check():

    crypto = Coin('Bitcoin', 'BTC')

    assert crypto.symbol_check() == 'Valid'

    crypto = Coin('Bitcoin2', 'BTC2')
    assert crypto.symbol_check() =='Valid'

    crypto = Coin('unselected', 'BTC')
    with pytest.raises(SymbolNameError):
        crypto.symbol_check()

    crypto = Coin('coinname', '12345')
    with pytest.raises(SymbolNameError):
        crypto.symbol_check()

    crypto = Coin('coinname', '12345678901')
    with pytest.raises(SymbolNameError):
        crypto.symbol_check()

    crypto = Coin('coinname', 'sdnetsvafee')
    with pytest.raises(SymbolLengthError):
        crypto.symbol_check()        

    
    