class Loggable:
    def __init__(self):
        self.title = ''

    def log(self):
        print('Log message from ' + self.title)


class Connection:
    def __init__(self):
        self.server = ''

    def connect(self):
        print('Connecting to database on  ' + self.server)


class SqlDatabase(Loggable, Connection):
    def __init__(self):
        self.title = 'sql connect demo'
        self.server = 'some_sqlserver'


def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()


sql_connect = SqlDatabase()
framework(sql_connect)
