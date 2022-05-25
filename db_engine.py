class DbEngine:
    def __init__(self, db_name, db_type="sqlite"):
        if db_type == "sqlite":
            import sqlite3 as sq
            try:
                self.__con = sq.connect(db_name)
                self.__cur = self.__con.cursor()
            except Exception as e:
                print(e)

    def __del__(self):
        if self.__con:
            self.__con.close()

    def execute_query(self, query, params=None):
        try:
            if params is None:
                self.__cur.execute(query)
            else:
                self.__cur.execute(query, params)
        except Exception as e:
            print(e)

    def rollback(self):
        self.__con.rollback()

    def commit(self):
        self.__con.commit()
