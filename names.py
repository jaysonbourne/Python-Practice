print("I am at Starbucks.")

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for players in students:
    print (players['first_name'], players['last_name'])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def printPlayers(inputs):
     for key in inputs:
         print (key)
         counter = 0
         for item in inputs[key]:
             counter += 1
             fullNameLength = len(item["first_name"])
             lastNameLenght = len(item["last_name"])
             print(counter, "-", item["first_name"], item["last_name"], "-", (fullNameLength+lastNameLenght))
printPlayers(users)
