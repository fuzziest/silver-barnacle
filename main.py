import requests
from dotenv import dotenv_values

env = dotenv_values()
host = 'https://api.pokemonbattle.me/v2'
headers = {
    'Content-Type': 'application/json',
    'trainer_token': env['TOKEN'],
}

response = requests.request(
    method='POST',
    url=f'{host}/pokemons',
    headers=headers,
    json={
        "name": "Бульбазавр",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    },
)
pokemonId = response.json()['id']
print(response.text)

response = requests.request(
    method='PUT',
    url=f'{host}/pokemons',
    headers=headers,
    json={
        "pokemon_id": pokemonId,
        "name": "New Name",
        "photo": "https://dolnikov.ru/pokemons/albums/008.png"
    },
)
print(response.text)

response = requests.request(
    method='POST',
    url=f'{host}/trainers/add_pokeball',
    headers=headers,
    json={
        "pokemon_id": pokemonId,
    },
)
print(response.text)
