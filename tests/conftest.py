import pytest
from main import app
@pytest.fixture()
def client ():
    """Fixture to set up a test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


