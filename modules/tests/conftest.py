import pytest
from ..database import Database as db

@pytest.fixture(scope="module")
def db_connection():
    dbase = db(ronly=False)
    yield dbase
    dbase.cur.close()
    dbase.conn.close()
    

@pytest.fixture(scope="module")
def next_coin_id


docker run --init -d \
  --name homeassistant \
  --restart=unless-stopped \
  -v /etc/localtime:/etc/localtime:ro \
  -v /home-assistant:/config \
  --network=host \
  homeassistant/raspberrypi4-homeassistant:stable