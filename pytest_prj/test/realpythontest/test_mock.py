from service import get_todos
from unittest import mock


def test_request_response_without_mock():
    response = get_todos()
    assert response is not None


@mock.patch('service.requests.get')
def test_request_response_with_mock(mock_get):
    mock_get.return_value.ok = True

    response = get_todos()
    assert response is not None
