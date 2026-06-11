capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary

# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

# print D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France" : {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany" : {
        "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
        "num_times_visited" : 5
    },
}

print(travel_log["Germany"]["cities_visited"][0])