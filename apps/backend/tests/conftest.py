import pytest

from app import create_app
from app.extensions import db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/test_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "RedisCache"  # disable Redis for tests
    CACHE_DEFAULT_TIMEOUT = 1  # short timeout
    FE_HOST = "localhost"  # not really used in tests


@pytest.fixture
def app():
    app = create_app(config_class=TestConfig)

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
