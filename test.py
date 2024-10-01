import pytest
from main import get_random_cat_image


def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id":"343",
        "url":"https://cdn2.thecatapi.com/images/343.gif",
        "width":100,
        "height":100
    }

    user_data = get_random_cat_image()

    assert user_data == {
        "id":"343",
        "url":"https://cdn2.thecatapi.com/images/343.gif",
        "width":100,
        "height":100
    }


def test_get_random_cat_image_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_random_cat_image()
   assert user_data == None

