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
    Column("id", String(64), primary_key=True),
    Column("user_name", String(50)),
    Column("user_phone", Integer),
    Column("user_password", String(255)),
    Column("user_creat_time", DateTime),
    Column("user_last_login_time", DateTime),
    Column("user_last_ip", String(50)),
    Column("user_vip_end_time", DateTime),
)

CiTanTask = Table(
    "citan_task",
    metadata,
    Column("task_id", Integer, primary_key=True),
    Column("user_id", String(64)),
    Column("account_number", String(128)),
    Column("account_password", String(128)),
    Column("server1", String(128)),
    Column("server2", String(128)),
    Column("task_change_time", DateTime),
    Column("task_start_time", Integer),
    Column("task_status", String(64)),
)

CiTanTaskLog = Table(
    "citan_task_log",
    metadata,
    Column("log_id", Integer, primary_key=True),
    Column("task_id", String(64)),
    Column("account_number", String(128)),
    Column("account_password", String(128)),
    Column("server1", String(128)),
    Column("server2", String(128)),
    Column("log_time", DateTime),
    Column("log_status", String(64)),
)

VipCouponse = Table(
    "vip_couponse",
    metadata,
    Column("id", String(64), primary_key=True),
    Column("create_time", DateTime),
    Column("activate_time", DateTime),
    Column("activate_user_id", String(128)),
    Column("creater_phone", String(128)),
    Column("order_id", Integer),
    Column("status", Integer),
)

OrderDb = Table(
    "pay_order",
    metadata,
    Column("id", String(64), primary_key=True),
    # 流水id
    Column("order_id", String(64),comment="商户流水id"),
    Column("create_time", DateTime),
    Column("pay_time", DateTime),
    Column("user_id", String(64)),
    Column("buy_num", Integer),
    Column("status", Integer),
    Column("is_zhichong",Integer),
    Column("phone_num",String(15)),
)

# databases query builder
database = Database(DATABASE_URL)
