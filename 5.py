def change_char(str):

    char=str[0]
    str=str.replace(char,'$')
    str=char+str[1:]

    return str
word=input("Enter any word")
print("Before replacement: ",word)
print("After replacement: ",change_char(word))