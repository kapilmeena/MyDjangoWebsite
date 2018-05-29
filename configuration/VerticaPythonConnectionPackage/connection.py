import vertica_python as vp
import logging

logging.basicConfig(filename='gunicon-server.log', level=logging.WARNING,
                    format='[%(levelname)s]: [%(asctime)s] [%(message)s]', datefmt='%m/%d/%Y %I:%M:%S %p')


class DataBase:
    def __init__(self, database=None, config=None):
        self.database, self.config, self.conn, self.cursor, self.execute = database, config, None, None, None
        self.db_connect()

    def db_connect(self):
        try:
            self.conn = self.database.connect(**self.config)
            self.cursor = self.conn.cursor()
            self.execute = self.cursor.execute
        except ConnectionError as ex:
            logging.error('file : ' + __name__ + ', ' + str(ex))
        except Exception as ex:
            logging.error('file : ' + __name__ + ', ' + str(ex))

    def close(self):
        try:
            if self.conn.closed:
                try:
                    self.cursor.close()
                    self.conn.close()
                except Exception as ex:
                    logging.error('file : ' + __name__ + ', ' + str(ex))
        except Exception as ex:
            logging.error('file : ' + __name__ + ', ' + str(ex))

    def read_data(self, query):
        try:
           self.execute(query)
           return self.cursor.fetchall()
        except Exception as ex:
            logging.error('file : ' + __name__ + ', ' + str(ex))
            self.db_connect()
            self.execute(query, )
            return self.cursor.fetchall()

    def insert_data(self, query):
        try:
            self.execute(query)
            self.conn.commit()
        except Exception as ex:
            self.db_connect()
            self.execute(query)
            self.conn.commit()

    def update_data(self, query):
        self.insert_data(query=query)

    def delete_data(self, query):
        self.insert_data(query=query)

    def __del__(self):
        self.close()


class Vertica(DataBase):
    """
    Example:
        config = {
            "host"='xx.xx.xx.xx',
            "port"=xxxxxx,
            "user"='xxx',
            "database"='xxx',
            "password"='xxx'
        }

        vp = Vertica(config=config)
        data = vp.read_data(query='sql query')
    """
    def __init__(self, config=None):
        if not config:
            print(__doc__)
            raise Exception("Kindly provide config detail in json format, config should contain host, port user, database, password.")
        if not isinstance(config, dict):
            print(__doc__)
            raise Exception("config should be dict type.")
        if 'host' not in config:
            print(__doc__)
            raise Exception("Kindly provide host detail in config variable")
        if 'port' not in config:
            print(__doc__)
            raise Exception("Kindly provide port detail in config variable")
        if 'user' not in config:
            print(__doc__)
            raise Exception("Kindly provide user detail in config variable")
        if 'database' not in config:
            print(__doc__)
            raise Exception("Kindly provide database detail in config variable")
        if 'password' not in config:
            print(__doc__)
            raise Exception("Kindly provide password detail in config variable")
        
        
        super(Vertica, self).__init__(vp, config)
        self.schema, self.table, self.sentence_column, self.occurrence_column = ('dev_analytics', 'sentence_prediction',
                                                                                 'sentence', 'occurrence')
