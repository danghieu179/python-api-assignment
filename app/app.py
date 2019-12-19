import falcon
from resources import CustomersCollectionResource, CustomersResource
from middleware.database import DatabaseCursor
from passlib.hash import sha256_crypt
from auth import sample_auth_jwt
from sqlalchemy import create_engine
from config import DATABASE_URL


def database_connection(db_url=DATABASE_URL):
    engine = create_engine(db_url)
    connection = engine.connect()
    return connection

# User for testing
USERS = {
    "danghieu1709@sample.test":
    {
        "email": "danghieu1709@sample.test",
        "password": sha256_crypt.encrypt("test")
    }
}
COOKIE_OPTS = {"name": "token",
               "max_age": 86400,
               "path": "/customers",
               "http_only": True}

login, auth_middleware = sample_auth_jwt.get_auth_objects(
    USERS.get,
    "please dont tell anyone",  # random secret
    3600,
    token_opts=COOKIE_OPTS)

app_middleware = [
    auth_middleware,
    DatabaseCursor(database_connection),
]

api = falcon.API(middleware=app_middleware)


# Add login resource
api.add_route('/login', login)

# Add api method
api.add_route('/customers', CustomersCollectionResource())
api.add_route('/customers/{id_:int}', CustomersResource())