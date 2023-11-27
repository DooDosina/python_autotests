import pytest
import requests

def test_satus_code():
    url = "https://api.pokemonbattle.me:9104/trainers"
    response = requests.get(url)
    assert response.status_code == 200

"""data = [{"trainer_name"}, "doodosina", "3599"]
@pytest.mark.parametrize("key", "value", "id", data)"""

def test_namecheck():
    url = "https://api.pokemonbattle.me:9104/trainers?trainer_id=3599"
    response = requests.get(url)
    response = response.json()
    assert response["trainer_name"] == "doodosina"
