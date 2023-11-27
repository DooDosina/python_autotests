import requests

url = "https://api.pokemonbattle.me:9104/pokemons"
pok_create = requests.post(url, json ={"name": "Tago","photo": "https://dolnikov.ru/pokemons/albums/003.png"}, 
                         headers = {'Content-Type':'application/json', 'trainer_token': '80cbccb8c59bd6658d0f9dce38de7ee8'},
                         timeout = 5)
print(f'Code: {pok_create.status_code} - {pok_create.reason}. Message: {pok_create.text}')

url = "https://api.pokemonbattle.me:9104/pokemons"
response = requests.put(url, json ={
                                "pokemon_id": "20717",
                                "name": "New Name",
                                "photo": "https://dolnikov.ru/pokemons/albums/008.png"},
                         headers = {'Content-Type':'application/json', 'trainer_token': '80cbccb8c59bd6658d0f9dce38de7ee8'},
                         timeout = 5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

url = "https://api.pokemonbattle.me:9104/trainers/add_pokeball"
response = requests.post(url, json ={"pokemon_id": "20717"}, 
                         headers = {'Content-Type':'application/json', 'trainer_token': '80cbccb8c59bd6658d0f9dce38de7ee8'},
                         timeout = 5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

