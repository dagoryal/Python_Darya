from sqlalchemy import create_engine, text

class DbTable:

    __scripts = {
        "select": text("select * from subject"),
        "new sub": text("insert into subject (subject_title, subject_id) values (:title, :id)"),
        "get max_id": text("select max (\"subject_id\") from subject"),
        "delete by id": text("delete from subject where subject_id =:id_to_delete"),
        "update": text("update subject set subject_title = :new_title where subject_id =:id"),
        "by id": text("select * from subject where subject_id =:main_id")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subject(self):
        with self.db.connect() as connection:
            res = connection.execute(self.__scripts["select"])
            return res.mappings().all()

    def create(self, s_title, s_id):
        with self.db.connect() as connection:
            transaction = connection.begin()

            connection.execute(self.__scripts["new sub"], {"title": s_title, "id": s_id})
            transaction.commit()
            connection.close()

    def get_max_id(self):
        with self.db.connect() as connection:
            return connection.execute(self.__scripts["get max_id"]).fetchall()[0][0]

    def delete(self, sub_id):
        with self.db.connect() as connection:
            transaction = connection.begin()

            connection.execute(self.__scripts["delete by id"], {"id_to_delete": sub_id})
            transaction.commit()
            connection.close()

    def edit(self, s_title, s_id):
        with self.db.connect() as connection:
            transaction = connection.begin()

            connection.execute(self.__scripts["update"], {"new_title": s_title, "id": s_id})
            transaction.commit()
            connection.close()

    def select_by_id(self, s_id):
        with self.db.connect() as connection:
            return connection.execute(self.__scripts["by id"], {"main_id": s_id}).fetchall()[0][0]
