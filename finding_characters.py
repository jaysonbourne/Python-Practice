#write a function that will find a character in a given list and then print the words with the character in it.

def find_characters(word_list, char):
    new_list = []
    for val in word_list:
        word = val
        if val.find(char) != -1:
            new_list.append(word)
            # print(new_list)
    return (new_list)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
print (find_characters(word_list, char))
