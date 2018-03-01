print("Making dictionaries.")

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict ={}
    #code here
    if len(list1) >= len(list2):
        for x in range(len(list1)):
            if x >= len(list2):
                new_dict[list1[x]] = ""
            else:
                new_dict[list1[x]] = list2[x]
    else:
        for x in range(len(list1)):
            if x >= len(list1):
                new_dict[list2[x]] = ""
            else:
                new_dict[list2[x]] = list1[x]
    return new_dict

print(make_dict(name, favorite_animal))
