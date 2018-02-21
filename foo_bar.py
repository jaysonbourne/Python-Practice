print ("hello world.")
# the i**.5 part is an exponation.

def foo_bar(min, max):
    for i in range(min, max+1):
        square = i**.5
        prime = True
        for j in range(2, int(square)+1):
            if i%j == 0:
                prime = False
                break
        if prime:
            print (i, " foo")
        elif square == round(square):
            print (i, " bar")
        else:
            print ( i, " foo bar")

print (foo_bar(1,100))
