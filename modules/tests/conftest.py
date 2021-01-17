import pytest
from ..database import Database as db

@pytest.fixture(scope="module")
def db_connection():
    dbase = db(ronly=False)
    yield dbase
    dbase.cur.close()
    dbase.conn.close()
    