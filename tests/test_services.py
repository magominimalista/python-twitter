from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

from main import app
from src.services import save_trends, get_trends_from_mongo

client = TestClient(app)


def test_get_trends_route():
    response = client.get("/trends")
    assert response.status_code == 200


def test_save_trends_route():
    mock_api = MagicMock()
    mock_trends = [{"name": "#trend1", "url": "http://example.com/trend1"},
                   {"name": "#trend2", "url": "http://example.com/trend2"}]
    mock_api.get_place_trends.return_value = [{"trends": mock_trends}]

    with patch("src.dependencies.get_tweepy_api", return_value=mock_api):
        response = client.post("/save_trends/")
        assert response.status_code == 200
        assert response.json() == {"status": "success"}


def test_get_trends_from_mongo():
    mock_trends = [{"name": "#trend1", "url": "http://example.com/trend1"},
                   {"name": "#trend2", "url": "http://example.com/trend2"}]

    with patch("src.connection.trends_collection.find", return_value=mock_trends):
        trends = get_trends_from_mongo()
        assert trends == mock_trends


def test_save_trends():
    mock_api = MagicMock()
    mock_trends = [{"name": "#trend1", "url": "https://example.com/trend1"},
                   {"name": "#trend2", "url": "https://example.com/trend2"}]
    mock_api.get_place_trends.return_value = [{"trends": mock_trends}]

    with patch("src.connection.trends_collection.insert_many") as mock_insert_many:
        save_trends(mock_api)
        mock_insert_many.assert_called_once_with(mock_trends)
