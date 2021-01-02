import psycopg2

class Database(object):

    def __init__(self, dev=os.environ['DEV']):
        
        if dev == 'PROD':
            self.dbname = os.environ['DB_NAME']
            self.host = os.environ['DB_HOST']
            self.user = os.environ['DB_USER']
            self.password = os.environ['DB_PASS']
            self.port = os.environ['DB_PORT']
            self.conn = psycopg2.connect(dbname=self.dbname, host=self.host, user=self.user, password=self.password, port=self.port)
            self.cur = self.conn.cursor()
            self.errors = psycopg2.errors
        elif dev == 'DEV':
            self.dbname = os.environ['DEV_DB_NAME']
            self.host = os.environ['DEV_DB_HOST']
            self.user = os.environ['DEV_DB_USER']
            self.password = os.environ['DEV_DB_PASS']
            self.port = os.environ['DEV_DB_PORT']
            self.conn = psycopg2.connect(dbname=self.dbname, host=self.host, user=self.user, password=self.password, port=self.port)
            self.cur = self.conn.cursor()
            self.errors = psycopg2.errors
        self.wallet_table='crypto.wallet'

    def add_wallet(self,coin_id, wallet_type, exchange_id, address):
        """Adds a wallet to the DB using coin_id, wallet_type (cold, exchange, etc.), exchange id, 
           and wallet address.

        Args:
            coin_id ([int]): numerical coin_id from database that represents a given coin
            wallet_type ([string]): cold (for cold storage) or exchange
            loc ([string]): If located on an exchange the exchange is supplied
            address ([string]): [description]

        Returns:
            [type]: [description]
        """
        wallet_sql=f"INSERT INTO {self.wallet_table} (coin_id, type, loc, address) VALUES ({coin_id},{wallet_type}, {loc}, {address}) RETURNING id;"
        try:
            self.cur.execute(wallet_sql)
        except self.errors.UniqueViolation as e:
            wallet_id = e
            return wallet_id
        else:
            self.conn.commit()
            wallet_id = self.cur.fetchone([0])
            self.cur.close()
        finally:
            self.conn.close
            return wallet_id

    def get_coin_id(self, symbol):
        """Finds and returns coin_id when supplied the symbol (BTC, XRP, etc.)

        Args:
            symbol ([string]): Coin market symbol (i.e. BTC, XRP)
        """

