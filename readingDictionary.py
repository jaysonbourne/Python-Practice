print("Skynet forever.")
# NOTE:****** IF you are looking for the answers to the assignment and not my notes jump down to line 39~****

#******EXAMPLE OF NESTED DICTIONARY*********
context = {
    'questions':[
    {'id': 1, 'content': "Why is there a light in the fridge?"},
    {'id': 2, 'content': "Why is there a light anywhere?"},
    {'id': 3, 'content': "What is life?"},
    ]
}
for key, data in context.items():
    for value in data:
        print("Question #", value["id"], ":", value["content"])
        print ("----")

# **********LIST FROM DICTIONARY***********
data = {"house":"Haus", "cat":"katze", "red":"rot"}
print(data.items())
print(data.keys())
print(data.values())

# *******DICTIONARIES FROM LISTS************
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_special = list(zip(countries, dishes))
print(country_special)
#NOTE: the zip function in python 3 needs to be unzipped, or it will give you a strange output like <zip object at some weird gibberish>. but by putting list in front of it you "exhaust" the zip function and it'll unpack its goodies.

# ---------------------USING THE DICT() FUNCTION--------------------
soda = ["Pepsi", "Coca-Cola", "Fanta", "Sprite"]
flavor = ["Ginger-Ale", "Cherry", "Pineapple", "Lemon-Lime"]
sodaFlavors = list(zip(soda, flavor))
# print (sodaFlavors)
sodaFlavors_dict = dict(sodaFlavors)
# print(sodaFlavors_dict)

# ----------------THE ACTUAL ASSIGNMENT IS DOWN HERE-----------------
profile = {
"Name":"Julie",
"Age":"27",
"JobStatus": "looking",
"Language": "Python"
}
print(profile.keys())
print(profile.items())
print(profile.values())
print("-----------------")
print("My name is {}. I am {} and I am currenlty {} for a job, And I like {}.".format(profile["Name"],profile["Age"], profile["JobStatus"], profile["Language"]))
