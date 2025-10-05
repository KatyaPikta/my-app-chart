import pytest

from app import create_app
from app.extensions import db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # in-memory DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "SimpleCache"  # disable Redis for tests
    CACHE_DEFAULT_TIMEOUT = 1  # short timeout
    FE_HOST = "localhost"  # not really used in tests

class RealServicesTestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/test_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "RedisCache"  # use real Redis
    CACHE_REDIS_HOST = "127.0.0.1"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_DEFAULT_TIMEOUT = 1
    FE_HOST = "127.0.0.1"

@pytest.fixture
def app():
    if os.getenv('USE_REAL_SERVICES'):
        app = create_app(RealServicesTestConfig)
    else:
        app = create_app(TestConfig)
        
    # Create tables before running tests
    with app.app_context():
        db.create_all()
    yield app

    # Drop tables after tests
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
