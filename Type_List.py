print ("hello world")

# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

#If a list is mixed ( integers, strings, etc. then the output should be "Mixed list and put out a sum.")

#difficulty of this would be sorting and then adding to get the sum correctly. \

varList = ['magical unicorns',19,'hello',98.98,'world']
y = [2,3,1,7,4,12]
z = ['magical', 'unicorns']

# def Type_list(varList):
#     result = "String: "
#     sum = 0
#     ints = 0
#     strings = 0
#     for val in varList:
#         if isinstance(val, str):
#             strings += 1
#             result += val + " "
#         elif isinstance(val, int) or isinstance(val, float):
#             ints += 1
#             sum += val
#     if ints !=0 and strings !=0:
#         print ("this list is of mixed type.")
#         print (result)
#         print ("Sum: "+ str(sum))

def Type_list(arr):
    if not arr:
        print ("Empty String.")
        return
    string =""
    total = 0

    for i in arr:
        if type(i) == str:
            string += i
        elif (type(i) == int) or (type(i) == float):
            total += i

    if (total and string):
        x = "mixed"
    else:
        if type(i) == str:
            x = "string"
        elif (type(i) == int) or (type(i) == flaot):
            x = "integer"

    print ("the list you entered is of " + str(x) + " type.")
    if string:
        print ("string: " + string)
    if total:
        print("Sum: "+ str(total))

Type_list(varList)
