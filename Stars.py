print("I was wrong Terminator could happen.")

def draw_stars(list):
    for i in list:
        if(isinstance(i, int)):
            print("*" * i)
        if(isinstance(i, str)):
            print(i[0]*len(i))
        else:
            continue
draw_stars(["apple", 4, "pineapple", 1,2,3])
