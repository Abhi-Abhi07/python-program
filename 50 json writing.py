import json
import pickle

s='''[
  {
    "userId": 1,
    "id":1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehebdeerif",
    "body": "quia et suscipit\nsuscipit recsandea conseqquunter expedita et cum\nreprehebderit mile\n"
  },
  {
    "userId": 1,
    "id":2,
    "title": "qui set esse",
    "body": "esse rerum tempre vitae\nsequl sint nihil reprehenderit dolor beatae ea dolores neque\nreprehebderit esse\n"
  },
  {
    "userId": 1,
    "id":3,
    "title": "ea molestaias quasi execritationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omins eligendi aut ad\nreppersent it ipsa sit\n"
  },
  {
    "userId": 1,
    "id":4,
    "title": "enum et est occaecati",
    "body": "ullam et seape reiciendis voluptatm adipisci\nsit auto matic\nreprehebderit est occaecati\n"
  }
]'''

file=open("posts.json","w")

file.write(s)


