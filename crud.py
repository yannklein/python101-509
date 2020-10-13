# CRUD on list
# beatles = ['john', 'paul', 'ringo']
# print(beatles)

# # Create
# beatles.append('george')
# print(beatles)

# # Read Paul
# print(beatles[1])
# print(beatles[1:3])
# print(beatles[1:])

# # Update
# beatles[2] = "Mango"
# print(beatles)

# # Delete
# del beatles[0]
# print(beatles)

# beatles = "oops"
# print(beatles)


# # CRUD on dict
# instruments = {'john':'guitar', 'paul':'bass'}
# print(instruments)

# # Create
# instruments['ringo'] = "drum"
# print(instruments)

# # Read Paul
# print(instruments["paul"])

# # Update
# instruments['paul'] = ["bass", "guitar"]
# print(instruments)

# # Delete
# del instruments['john']
# print(instruments)

beatles = {
    "john": {
        "instruments": ["bass", "guitar"],
        "age": 24
    },
    "paul": {
        "instruments": ["drum", "triangle"],
        "age": 32
    }
}

# print(beatles["john"]["instruments"][1])

# beatles_list = [
#     {
#         "name": "John",
#         "instruments": ["bass", "guitar"],
#         "age": 24
#     },
#     {
#         "name": "Paul",
#         "instruments": ["drum", "triangle"],
#         "age": 32
#     }
# ]

instruments = {'john':'guitar', 'paul':'bass'}
# print(instruments['ringo'])
print(instruments.get('john', 'Not found'))
name = "ringo"
print(instruments.get(name, f'Not found {name}'))
name = "yann"
print(instruments.get(name, f'Not found {name}'))

