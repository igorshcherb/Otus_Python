import os

PG_CONN_URL = os.environ.get("PG_CONN_URL", default="user:password@localhost:5432/db01")

PG_CONN_URI = (
        os.environ.get("SQLALCHEMY_PG_CONN_URI")
        or f"postgresql+asyncpg://{PG_CONN_URL}"
)

BASE_API_URL = "http://jsonplaceholder.typicode.com"

SQLALCHEMY_ECHO = False

SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 10

SQLA_NAMING_CONVENTIONS = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
