print("hello world.")

def odd_even():
    for x in range(1,50):
        if x%2 ==0:
            print ("Number is {}. This is an even number.".format(x))
        else:
            print("Number is {}. This is an odd number.".format(x))


def multiply(arr, j):
    new_str = []
    for j in arr:
        new_str.append(j*5)
    return new_str
a = [1,200,3,4]
b = multiply(a,5)
print (b)
