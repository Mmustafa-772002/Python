# trasnltor in python is a tool that converts the code from one language to another language

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEOIUaeoiu":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
            
    return translation
print(translate(input("Enter a phrase: ")))