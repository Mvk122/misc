xdef multiply(a,b):
    x = 0
    for _ in range(b):
        x += a
    return x

def factorial(a):
    if a == 1:
        return 1
    else:
        return a* factorial(a-1)


import string
def build_shift_dict(shift):
    LowerCaseinitial = string.ascii_lowercase
    shift_dict = {}
    Uppercaseinitial = string.ascii_uppercase
    for i in range(len(LowerCaseinitial)):
        if i < len(LowerCaseinitial) - shift:
            shift_dict[LowerCaseinitial[i]] = LowerCaseinitial[i + shift]
        else:
            shift_dict[LowerCaseinitial[i]] = LowerCaseinitial[abs(26 - (i + shift))]
    for i in range(len(Uppercaseinitial)):
        if i < len(Uppercaseinitial) - shift:
            shift_dict[Uppercaseinitial[i]] = Uppercaseinitial[i + shift]
        else:
            shift_dict[Uppercaseinitial[i]] = Uppercaseinitial[abs(26 - (i + shift))]
    return shift_dict

def apply_shift_dict(message, shift):
    encrypted = ""
    shift_dict = build_shift_dict(shift)
    for letter in message:
        if letter in shift_dict.keys():
            encrypted += shift_dict[letter]
        else:
            encrypted += letter

    return encrypted

def remove_shift(message, shift):
    shift = 26 - shift
    encrypted = ""
    shift_dict = build_shift_dict(shift)
    for letter in message:
        if letter in shift_dict.keys():
            encrypted += shift_dict[letter]
        else:
            encrypted += letter

    return encrypted

def testsubject(variable = 5): #default arguments can be used if a user does not add an argument to a function
    return variable ** 2
def build_dict(vowels_permutation):
    vowels = "aeiou"
    voweldict = {}
    for letter in vowels_permutation:
        voweldict[letter] = vowels[vowels_permutation.index(letter)]
        voweldict[letter.upper()] = vowels[vowels_permutation.index(letter)].upper()
    return voweldict


def is_phrase_in(story, phrase="purple cow"):
    def replacewithspace(text):
        text = text.lower()
        newtext = ''
        for letter in text:
            if letter in string.punctuation:
                newtext += " "
            else:
                newtext += letter
        return newtext
    story = replacewithspace(story).split(" ")
    story = [x for x in story if x != ""]
    phrase = replacewithspace(phrase).split(" ")
    phrase = [x for x in phrase if x != ""]
    if phrase[0] in story:
        initialIndex = story.index(phrase[0])
        for i in range(len(phrase)):
            try:
                if story[initialIndex + i] != phrase[i]:
                    return False
            except:
                return False
        return True
    else:
        return False


print(is_phrase_in('PURPLE COW', "purple!cow"))
print(is_phrase_in('The purple cow is soft and cuddly.'))
print(is_phrase_in("purple@#$%cow'"))
print(is_phrase_in('Cow!!! Purple!!!'))
print(is_phrase_in('purplecowpurplecowpurplecow'))
print(is_phrase_in('purple cows are cool'))
