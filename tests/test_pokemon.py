import requests
import pytest
from dotenv import dotenv_values

env = dotenv_values()
host = 'https://api.pokemonbattle.me/v2'
headers = {
    'Content-Type': 'application/json',
    'trainer_token': env['TOKEN'],
}


def test_get_trainers():
    response = requests.request(
        method='GET',
        url=f'{host}/trainers',
        headers=headers,
    )
    assert response.status_code == 200


def test_my_trainer_name():
    response = requests.request(
        method='GET',
        url=f'{host}/trainers',
        headers=headers,
        params={
            'trainer_id': '2820'
        }
    )
    assert response.json()['data'][0]['trainer_name'] == 'персик'
