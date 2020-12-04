import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.sql import func

from databases import Database
import sys

if sys.platform == "win32" or sys.platform == "win64":
    import demo_config
    DATABASE_URL = demo_config.DATABASE_URL
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

TableUser = Table(
    "table_user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(50)),
    Column("user_phone", Integer),
    Column("user_password", String(255)),
    Column("user_creat_time", DateTime),
    Column("user_last_login_time", DateTime),
    Column("user_last_ip", String(50)),

)

# databases query builder
database = Database(DATABASE_URL)
