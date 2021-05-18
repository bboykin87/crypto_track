import pytest
from ..coin import Coin
from ..errors import CoinNameError, SymbolNameError, CoinLengthError, SymbolLengthError, CoinIdError

def test_coin_name_check():

    #  Valid tests
    crypto = Coin('Bitcoin', 'BTC')

    assert crypto.coin_name_check() == 'Valid'

    crypto = Coin('Bitcoin2', 'BTC2')
    assert crypto.coin_name_check() =='Valid'

    # Invalid tests
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

    crypto = Coin('sed kjas', 'BTC')
    with pytest.raises(CoinNameError):
        crypto.coin_name_check()



def test_symbol_check():

    crypto = Coin('Bitcoin', 'BTC')

    assert crypto.symbol_check() == 'Valid'

    crypto = Coin('Bitcoin2', 'BTC2')
    assert crypto.symbol_check() =='Valid'

    crypto = Coin('sadds', 'unselected')
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

    crypto = Coin('deswasd', 'B TC')
    with pytest.raises(SymbolNameError):
        crypto.symbol_check()

def test_id_check():

    crypto = Coin(id=4321)
    assert crypto.id_check() == 'Valid'

    crypto = Coin(id=0)
    with pytest.raises(CoinIdError):
        crypto.id_check()

    crypto = Coin(id='dec')
    with pytest.raises(CoinIdError):
        crypto.id_check()

    crypto = Coin(id=32)
    with pytest.raises(CoinIdError):
        crypto.id_check()

    crypto = Coin(id=32490)
    with pytest.raises(CoinIdError):
        crypto.id_check()

    crypto = Coin(id=33.4)
    with pytest.raises(CoinIdError):
        crypto.id_check()

def test_coin_create(db_connection):
    coin=Coin('Bitcoin', 'BTC')
    assert coin.symbol_check() == 'Valid'
    assert coin.coin_name_check() == 'Valid'
    coin_id_sql = f'SELECT id FROM crypto.coins'
    db_connection.cur.execute(coin_id_sql)
    r = db_connection.cur.fetchone()
    # coin_create should check symbol and coin name and return coin_id
    assert coin.coin_create(coin.coin_name, coin.symbol) == 