from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config


class NebulaSession:
    def __init__(self, host: str = '127.0.0.1', user: str = 'root', password: str = 'nebula'):
        self.host = host
        self.user = user
        self.password = password
        self.connection_pool = None
        self.session = None
        self.open_session()

    def open_session(self):
        # define a config
        config = Config()
        config.max_connection_pool_size = 10
        # init connection pool
        self.connection_pool = ConnectionPool()
        # if the given servers are ok, return true, else return false
        ok = self.connection_pool.init([(self.host, 9669)], config)

        # option 1 control the connection release yourself
        # get session from the pool
        self.session = self.connection_pool.get_session(self.user, self.password)

    def close_session(self):
        # release session
        self.session.release()
        # close the pool
        self.connection_pool.close()
