import uuid
from datetime import datetime
from functools import partial

from sqlalchemy import Table, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.event import listen

from app import db


def create_partition(target, connection, **kw) -> None:
    """ creating partition by users_history """

    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_01" PARTITION OF "users_history" FOR VALUES FROM ('2022-01-01') TO ('2022-02-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_02" PARTITION OF "users_history" FOR VALUES FROM ('2022-02-01') TO ('2022-03-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_03" PARTITION OF "users_history" FOR VALUES FROM ('2022-03-01') TO ('2022-04-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_04" PARTITION OF "users_history" FOR VALUES FROM ('2022-04-01') TO ('2022-05-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_05" PARTITION OF "users_history" FOR VALUES FROM ('2022-05-01') TO ('2022-06-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_06" PARTITION OF "users_history" FOR VALUES FROM ('2022-06-01') TO ('2022-07-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_07" PARTITION OF "users_history" FOR VALUES FROM ('2022-07-01') TO ('2022-08-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_08" PARTITION OF "users_history" FOR VALUES FROM ('2022-08-01') TO ('2022-09-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_09" PARTITION OF "users_history" FOR VALUES FROM ('2022-09-01') TO ('2022-10-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_10" PARTITION OF "users_history" FOR VALUES FROM ('2022-10-01') TO ('2022-11-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_11" PARTITION OF "users_history" FOR VALUES FROM ('2022-11-01') TO ('2022-12-01')"""
    )
    connection.execute(
        f"""CREATE TABLE IF NOT EXISTS "users_history_2022_12" PARTITION OF "users_history" FOR VALUES FROM ('2022-12-01') TO ('2023-01-01')"""
    )


class UsersHistory(db.Model):
    __tablename__ = "users_history"
    __table_args__ = (
        UniqueConstraint('id', 'auth_date'),
        {
            'postgresql_partition_by': 'RANGE (auth_date)',
        }
    )

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    user_id = db.Column(db.Integer)
    user_agent = db.Column(db.String(150))
    auth_date = db.Column(db.DateTime, default=datetime.utcnow, primary_key=True)

    def __repr__(self):
        return f"<UsersHistory {self.id} {self.user_id} {self.user_agent} {self.auth_date}>"


def on_table_create(class_, ddl):

    def listener(tablename, ddl, table, bind, **kw):
        if table.name == tablename:
            ddl(table, bind, **kw)

    listen(Table, 'after_create', partial(listener, class_.__table__.name, ddl))


on_table_create(UsersHistory, create_partition)
