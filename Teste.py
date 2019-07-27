# -*- coding: utf-8 -*-
import unirest


msg = u'Possíveis aparições de ditto:\n\n'

response = unirest.get("https://pokemon-go1.p.rapidapi.com/possible_ditto_pokemon.json",
  headers={
    "X-RapidAPI-Host": "pokemon-go1.p.rapidapi.com",
    "X-RapidAPI-Key": "e9b0d5fec5msh4383c8fa32ee394p1b7c53jsn938b9968e3c7"
  }
)

for item in response.body:
    msg += response.body.get(item).get('name')+u'\n'

print(msg)