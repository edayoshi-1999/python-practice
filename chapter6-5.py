person = {"name": "bob", "age": 25, "favorite": "apple"}

for key, value in zip(person.keys(), person.values()):
    print(f"key: {key}, value:{value}")

for item in person.items():
    print(item)