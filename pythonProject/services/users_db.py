import sqlalchemy as db


class UserDatabase:
    def __init__(self, database_uri):
        self.engine = db.create_engine(database_uri)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.users = db.Table("users", self.metadata,
                       db.Column('user_id', db.Integer, primary_key=True),
                             db.Column('first_name', db.TEXT),
                             db.Column('last_name', db.TEXT),
                             )
        self.metadata.create_all(self.engine)

    async def add_user(self, user_id, first_name, last_name):
        if not await self.user_exists(user_id):
            insert_statement = self.users.insert().values(user_id=user_id, first_name=first_name, last_name=last_name)
            self.connection.execute(insert_statement)
            self.connection.commit()
        else:
            pass

    async def user_exists(self, user_id):
        select_statement = self.users.select().where(self.users.columns.user_id == user_id)
        result = self.connection.execute(select_statement)
        return result.fetchone() is not None


users_db = UserDatabase('sqlite:///users-db.db')

