person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print("key",":","values")
for key in person:
    print(key,":",person[key])

print("key",":","items")
for key in person.items():
    print(key[0],key[1])
