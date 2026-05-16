import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_store


@pytest.fixture
def client():
    original_activities = copy.deepcopy(activities_store)
    try:
        yield TestClient(app)
    finally:
        activities_store.clear()
        activities_store.update(original_activities)
