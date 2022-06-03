address = {"state": "Texas", 'city': 'Houston'}


dict={"name":"siri","age":21,"address":address}

print(dict)

print(dict["address"]["city"])

print("person details")
for key,value in dict.items():
    if key=="address":
        print("person address")
        for nested_key , nested_value in value.items():
          print(nested_key,":",nested_value)
    else:
        print(key,":",value)