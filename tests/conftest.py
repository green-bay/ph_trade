import pytest
from app import create_app
from app.db import db
from app.config import ConfigTest

@pytest.fixture
def app():
    app = create_app(ConfigTest)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
