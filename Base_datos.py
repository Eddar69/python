import psycopg2


class Database(object):

        def __init__(self, ip=None, port=5432, user=None, password=None, database=None):
                self.ip = ip
                self.port = port
                self.user = user
                self.password = password
                self.database = database
                self.conn = psycopg2.connect(database=self.database,
                                             user=self.user,
                                             password=self.password,
                                             host=self.ip,
                                             port=self.port)
                self.curt = self.conn.cursor()
        def execute_query(self, query, commit=False):
                self.curt.execute(query)
                if commit:
                       self.out.autocommit()
                return self.curt.fetchall()