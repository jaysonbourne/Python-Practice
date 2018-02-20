# Filter by type: If the integer is greater than or equal to 100 print "that's a big number" else print "thats a meh number"

x = 1
if x >= 100:
    print ("that's a big number")
else:
    print ("that's a small number")

# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

aString = "This is a sentence.This is a sentence.This is a sentence.This is a sentence.This is a sentence.This is a sentence."
bString = "volutpat avolutpat avolutpat avolutpat avolutpat "
if len(bString) >= 50:
    print ("that's a long sentence.")
else:
    print("that's a short sentence.")

# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#the tricky part to this is to separate lists into types, integers or strings or arrays.
def filterByType(typeToCompare):
    outputStr =''
    if isinstance(typeToCompare, int):
        if typeToCompare >= 100:
            outputStr = "Big number."
        else:
            outputStr = "Small number."
    elif isinstance(typeToCompare, str):
        if len(typeToCompare) >= 50:
            outputStr = "Long."
        else:
            outputStr ="Short."
    elif isinstance(typeToCompare, list):
        if len(typeToCompare) >= 10:
            outputStr = "Long list."
        else:
            outputStr = "Short list."
    else:
        print ("IDK the type!")
        print (typeToCompare)

    print (typeToCompare)
    print(outputStr + '\n') #\n means to create a new line.

filterByType(sI)
filterByType(spL)
